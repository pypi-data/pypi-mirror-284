import argparse
import sys
import os
import inquirer
from cxcli.customers.delete_customers import delete_customers_list, delete_customer
from cxcli.tools.api_utils.cx_caller import CxCaller
from cxcli.tools.io_utils import validate_file_path
from rich.console import Console
from rich import print

def prompt_for_status():
    allowed_status = ["Initialized", "Approved", "Activated"]
    questions = [
        inquirer.List('status',
                      message="Please choose a customer status",
                      choices=allowed_status,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['status']

def create_parser():
    parser = argparse.ArgumentParser(description="Business Units")
    parser.add_argument("cmd", choices=["delete"])
    return parser

def customer_cmd(cx: CxCaller, format, args, file=None, individual_id=None):
    console = Console()
    parser = create_parser()
    parsed_args = parser.parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd == "delete":
        if file:
            if validate_file_path(file, '.csv'):
                delete_customers_list(cx, os.path.abspath(file))
            else:
                sys.exit(1)
        elif individual_id:
            status = prompt_for_status()
            print(f"Processing for customer with individual ID: [yellow]{individual_id}[/] and status: [yellow]{status}[/]...")
            delete_customer(cx, individual_id, status)
        else:
            print("Error: No argument provided. Please provide argument --file or --individual_id")
