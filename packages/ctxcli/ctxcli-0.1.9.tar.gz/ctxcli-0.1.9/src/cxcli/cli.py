import argparse
import warnings

from cxcli import users
from cxcli import authentication
from cxcli import business_units
from cxcli import orders
from cxcli import business_units
from cxcli import billing
from cxcli import customers
from cxcli.authentication.auth import get_token_from_config, get_auth_config_field
from cxcli.tools.api_utils.cx_caller import ENVS, CxCaller, get_domain_name
from cxcli.migration import migration_cmd
from cxcli.tenant import tenants_cmd
from urllib3.exceptions import InsecureRequestWarning
from rich import print
from rich.console import Console


def create_parser():
    parser = argparse.ArgumentParser(
        description="ConnectX CLI", epilog="Copyright Amdocs"
    )
    parser.add_argument("--t", "--tenant", help="Tenant name")
    parser.add_argument("--u", "--user", help="ConnectX username (email in most cases)")
    parser.add_argument("--p", "--passw", help="ConnectX password")
    parser.add_argument(
        "--e",
        "--env",
        help=",".join(ENVS),
        choices=ENVS,
        type=str.lower,
    )
    parser.add_argument(
        "--format", default="table", choices=["json", "csv", "table"], type=str.lower
    )
    parser.add_argument(
        "command",
        choices=[
            "user",
            "tenant",
            "migration",
            "auth",
            "business-unit",
            "order",
            "authcheck",
            "billing",
            "customer"
        ],
        type=str.lower,
    )
    parser.add_argument(
        "--file", type=str, help="File path for input file to be processed"
    )
    parser.add_argument("--individual-id", type=str, help="Unique individual ID")
    parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    parser.add_argument("--output", type=str, help="Output Excel file path")
    parser.add_argument("params", nargs="*")
    return parser


def main():
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    try:
        args = create_parser().parse_args()
        if args.command == "auth":
            authentication.auth_cmd()
            return
        elif args.command == "authcheck":
            authentication.authcheck_cmd()
            return

        results = get_token_from_config()
        access_token = results[1]
        env = results[2]

        if not access_token:
            return
        domain_name = get_domain_name(env)
        cx = CxCaller(domain_name=domain_name, token=access_token)
        format = args.format
        if args.command == "user":
            users.users_cmd(cx, format, args.params)
        elif args.command == "tenant":
            tenants_cmd(cx, format, args.params)
        elif args.command == "migration":
            migration_cmd(cx, format, args.params)
        elif args.command == "business-unit":
            business_units.bu_cmd(cx, format, args.params, args.file)
        elif args.command == "order":
            orders.order_cmd(cx, format, args.params, args.start_date, args.end_date, args.output)
        elif args.command == "billing":
            billing.billing_cmd(cx, format, args.params)
        elif args.command == "customer":
            customers.customer_cmd(cx, format, args.params, args.file, args.individual_id)
        else:
            raise ValueError(f"Unknown command {args.command}")
        # print(token)
    except KeyboardInterrupt:
        print("")
