"""
Python3 script to search for Devices in the Inventory Table.
"""

import argparse
import json
import logging
import re
from typing import Dict, Union

from ipfabric import IPFClient
from ipfabric.scripts.shared import shared_args

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    raise ImportError("Rich is required for printing, please install by using `pip3 install rich`.")

CONSOLE = Console()

logging.basicConfig(format="%(levelname)s: %(message)s")

LOGGER = logging.getLogger("ipf_device_search")

VALID_COLUMNS = {
    "uptime": {"name": "uptime", "filter": "float", "alt_name": None},
    "model": {"name": "model", "filter": "str", "alt_name": None},
    "reload": {"name": "reload", "filter": "str", "alt_name": None},
    "image": {"name": "image", "filter": "str", "alt_name": None},
    "domain": {"name": "domain", "filter": "str", "alt_name": None},
    "platform": {"name": "platform", "filter": "str", "alt_name": None},
    "slug": {"name": "slug", "filter": "str", "alt_name": None},
    "hostname": {"name": "hostname", "filter": "str", "alt_name": None},
    "fqdn": {"name": "fqdn", "filter": "str", "alt_name": None},
    "processor": {"name": "processor", "filter": "str", "alt_name": None},
    "sn": {"name": "sn", "filter": "str", "alt_name": None},
    "version": {"name": "version", "filter": "str", "alt_name": None},
    "vendor": {"name": "vendor", "filter": "str", "alt_name": None},
    "family": {"name": "family", "filter": "str", "alt_name": None},
    "stpdomain": {"name": "stpDomain", "filter": "str", "alt_name": "stp_domain"},
    "hostnameoriginal": {"name": "hostnameOriginal", "filter": "str", "alt_name": "hostname_original"},
    "loginip": {"name": "loginIp", "filter": "str", "alt_name": "login_ip"},
    "snhw": {"name": "snHw", "filter": "str", "alt_name": "sn_hw"},
    "memorytotalbytes": {"name": "memoryTotalBytes", "filter": "float", "alt_name": "mem_total_bytes"},
    "hostnameprocessed": {"name": "hostnameProcessed", "filter": "str", "alt_name": "hostname_processed"},
    "sitename": {"name": "siteName", "filter": "str", "alt_name": "site"},
    "devtype": {"name": "devType", "filter": "str", "alt_name": "dev_type"},
    "tsdiscoveryend": {"name": "tsDiscoveryEnd", "filter": "float", "alt_name": "ts_discovery_end"},
    "configreg": {"name": "configReg", "filter": "str", "alt_name": "config_reg"},
    "rd": {"name": "rd", "filter": "str", "alt_name": "routing_domain"},
    "memoryusedbytes": {"name": "memoryUsedBytes", "filter": "float", "alt_name": "mem_used_bytes"},
    "memoryutilization": {"name": "memoryUtilization", "filter": "float", "alt_name": "mem_utilization"},
    "secdiscoveryduration": {"name": "secDiscoveryDuration", "filter": "float", "alt_name": "sec_discovery_duration"},
    "logintype": {"name": "loginType", "filter": "str", "alt_name": "login_type"},
    "tsdiscoverystart": {"name": "tsDiscoveryStart", "filter": "float", "alt_name": "ts_discovery_start"},
    "loginport": {"name": "loginPort", "filter": "int", "alt_name": "login_port"},
    "objectid": {"name": "objectId", "filter": "str", "alt_name": "object_id"},
    "taskkey": {"name": "taskKey", "filter": "str", "alt_name": "task_key"},
}
VALID_ALT_COLUMNS = {_["alt_name"]: _ for _ in VALID_COLUMNS.values()}
COLUMNS_HELP = [
    f"{_['name']}{'|' + _['alt_name'] if _['alt_name'] else ''} ({_['filter']})" for _ in VALID_COLUMNS.values()
]
DEFAULT_COLUMNS = [
    "hostname",
    "siteName",
    "vendor",
    "family",
    "platform",
    "model",
    "version",
    "loginIp",
    "snHw",
    "devType",
]
STR_OPERATORS = {
    "=": "eq",
    "!=": "neq",
    "i=": "ieq",
    "i!=": "nieq",
    "~": "like",
    "!": "notlike",
    "=~": "reg",
    "!=~": "nreg",
    "i=~": "ireg",
    "i!=~": "nireg",
}
INT_OPERATORS = {
    "=": "eq",
    "!=": "neq",
    ">": "gt",
    ">=": "gte",
    "<": "lt",
    "<=": "lte",
}


def main() -> Dict[str, Dict[str, Union[str, list]]]:
    arg_parser = argparse.ArgumentParser(
        description="Search the Inventory > Device table and return the results.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=f"""
Valid Column Names:
{json.dumps(COLUMNS_HELP, indent=2)}

String Operators:
{json.dumps(STR_OPERATORS, indent=2)}

Number Operators:
{json.dumps(INT_OPERATORS, indent=2)}
""",
    )
    arg_parser.add_argument(
        "search",
        help="Search value: 'ipf_device_search rtr1'. Default uses 'hostname' for search. "
        "Example for different column: 'ipf_device_search vendor cisco'.",
        nargs="+",
    )
    arg_parser.add_argument(
        "-o",
        "--operator",
        help="Operator used in searching; default is 'like'.",
        default="like",
    )
    arg_parser.add_argument(
        "-C",
        "--csv",
        help="Export to CSV format.",
        action="store_true",
        default=False,
    )
    arg_parser.add_argument(
        "-a",
        "--add-columns",
        help="Comma separated list of column names to add to output.",
        default=None,
    )
    arg_parser.add_argument(
        "-r",
        "--remove-columns",
        help="Comma separated list of column names to remove from output.",
        default=None,
    )
    args = shared_args(arg_parser)

    column, columns, search, operator = validate_args(args)
    columns = modify_columns(columns, args.add_columns, args.remove_columns)

    ipf = IPFClient(snapshot_id=args.snapshot)
    filters = {column: [operator, search]}
    if args.csv:
        print(ipf.inventory.devices.all(export="csv", filters=filters, columns=columns).decode())
        exit(0)

    results = ipf.inventory.devices.all(filters=filters, columns=columns)
    if args.json and args.rich_disable:
        print(json.dumps(results, indent=2))
    elif args.json:
        CONSOLE.print(results)
    else:
        rich_print(results, ipf.oas["tables/inventory/devices"].post.filter_url(filters), columns, args.count)


def modify_columns(columns: list, add: str, remove: str):
    cols = set(columns)
    if add:
        for _ in add.split(","):
            col = validate_column(_.lower())
            if col and col not in cols:
                columns.append(col)
    if remove:
        for _ in remove.split(","):
            col = validate_column(_.lower())
            if col and col in cols:
                columns.remove(_)
    return columns


def validate_column(column: str) -> str:
    if not column:
        return column
    if column not in VALID_COLUMNS and column not in VALID_ALT_COLUMNS:
        LOGGER.critical(
            f"Column '{column}' is not a valid column name. "
            f"Valid names:\n{json.dumps(sorted(COLUMNS_HELP), indent=2)}"
        )
        exit(1)
    return VALID_COLUMNS[column]["name"] if column in VALID_COLUMNS else VALID_ALT_COLUMNS[column]["name"]


def validate_operator(operator: str, col_filter: str):
    if col_filter == "str":
        if operator in STR_OPERATORS:
            operator = STR_OPERATORS[operator]
        elif operator not in STR_OPERATORS.values():
            LOGGER.critical(
                f"Operator '{operator}' is not valid for text column. "
                f"Valid operators:\n{json.dumps(list(STR_OPERATORS), indent=2)}"
            )
            exit(1)
    else:
        if operator in INT_OPERATORS:
            operator = INT_OPERATORS[operator]
        elif operator not in INT_OPERATORS.values():
            LOGGER.critical(
                f"Operator '{operator}' is not a valid for number column. "
                f"Valid operators:\n{json.dumps(list(INT_OPERATORS), indent=2)}"
            )
            exit(1)
    return operator


def validate_args(args: argparse.Namespace):
    if len(args.search) > 2:
        LOGGER.critical("Too many positional arguements given.")
        exit(1)
    elif len(args.search) == 1:
        column, search, col_filter = "hostname", args.search[0], "str"
    elif len(args.search) == 2:
        column, search = args.search[0].lower(), args.search[1]
        column = validate_column(column)
        col_filter = VALID_COLUMNS[column.lower()]["filter"]

    operator = validate_operator(args.operator.lower(), col_filter)

    columns = DEFAULT_COLUMNS.copy()
    if column not in columns:
        columns.append(column)
    if column in ["secDiscoveryDuration", "uptime"]:
        search = time_converter(search)
    return column, columns, search, operator


def time_converter(search: Union[str, int, float]) -> int:
    if isinstance(search, (int, float)):
        return int(search)
    TIME_DURATION_UNITS = {
        "year": 31557600,
        "month": 2629800,
        "week": 604800,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1,
    }
    TIME_CONVERTER = {
        **TIME_DURATION_UNITS,
        "y": TIME_DURATION_UNITS["year"],
        "mon": TIME_DURATION_UNITS["month"],
        "w": TIME_DURATION_UNITS["week"],
        "d": TIME_DURATION_UNITS["day"],
        "h": TIME_DURATION_UNITS["hour"],
        "min": TIME_DURATION_UNITS["minute"],
        "m": TIME_DURATION_UNITS["minute"],
        "sec": TIME_DURATION_UNITS["second"],
        "s": TIME_DURATION_UNITS["second"],
    }
    _ = re.findall(r"(\d*)\s?([a-z]*)", search.lower())

    seconds = 0
    for v, d in _:
        try:
            v = int(v)
        except ValueError:
            continue
        if d != "s" and d[-1] == "s":
            d = d[:-1]
        seconds += v * TIME_CONVERTER[d]

    return seconds


def rich_print(results: list, url: str, columns: list, count: bool = False):
    if count or not results:
        CONSOLE.print(f"Total rows: {str(len(results))}")
    if not count and results:
        table = Table(*columns, title="Device Inventory")
        for result in results:
            table.add_row(*[str(result[c]) for c in columns])
        CONSOLE.print(table)
    CONSOLE.print(url, style=f"link {url}")


if __name__ == "__main__":
    main()
