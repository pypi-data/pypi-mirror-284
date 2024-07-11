import argparse
import os
import sys
import datetime
from cxcli.tools.api_utils.cx_caller import CxCaller
from cxcli.orders.export_orders import export_orders


def usage():
    print ("Available commands: export")


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
    
def validate_output_path(output_path):
    output_dir = os.path.dirname(output_path)
    return os.path.exists(output_dir)
    
    
def create_parser():
    parser = argparse.ArgumentParser(description="Orders")
    parser.add_argument("cmd", choices=["export"])
    parser.add_argument("params", nargs="*")
    return parser


def order_cmd(cx: CxCaller, format, args, start_date, end_date, output ):
    parser = create_parser()
    parsed_args = parser.parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd=="export":
        if not start_date or not end_date or not output:
            print("start-date, end-date, and output are required parameters.")
            sys.exit(1)
        if not (validate_date(start_date) and validate_date(end_date)):
            print("Invalid date format. Use DD-MM-YYYY.")
            sys.exit(1)
        # if validate_output_path(output) == False:
        #     print(f"Output directory for '{output}' does not exist.")
        #     sys.exit(1)
        export_orders(cx, start_date, end_date, output)