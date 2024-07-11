import argparse
from cxcli.billing.bill import get_acbrs
from cxcli.tools.api_utils.cx_caller import CxCaller
from cxcli.users.list_users import list_users



def create_parser():
    parser = argparse.ArgumentParser(description="Users")
    parser.add_argument("cmd", choices=["acbrs"])
    parser.add_argument("params", nargs="*")
    return parser



def billing_cmd(cx: CxCaller, format, args):
    parsed_args = create_parser().parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd=="acbrs":
        get_acbrs(cx, format, parsed_args.params)


