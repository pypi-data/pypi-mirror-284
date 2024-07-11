import argparse
from cxcli import SRV_BILLING
from cxcli.tools.api_utils.cx_caller import CxCaller, Verb
from rich import print_json
import json
from rich.console import Console
from rich.table import Table


def acbrs_as_table(acbrs):
    table = Table(title="ACBRs")
    table.add_column("Id", no_wrap=True)
    table.add_column("Date", no_wrap=True,)
    table.add_column("Name", no_wrap=True,)
    table.add_column("Product", no_wrap=True)
    table.add_column("Net", no_wrap=True, justify="right")
    table.add_column("Tax", no_wrap=True, justify="right")
    table.add_column("Total", no_wrap=True, justify="right")
    table.add_column("Currency", no_wrap=True)
    for a in acbrs:
        n = a["taxExcludedAmount"]["value"]
        tot = a["taxIncludedAmount"]["value"]
        t = tot - n
        curr = a["taxExcludedAmount"]["unit"]
        table.add_row(a["id"],a["date"],a["name"],a["product"]["id"], f"{n:.2f}",f"{t:.2f}",f"{tot:.2f}",curr)
    console = Console()
    console.print(table)


def get_acbrs(cx: CxCaller, format: str, args):
    parser = argparse.ArgumentParser()
    parser.add_argument("billingaccount")
    parser.add_argument("bill")
    parsed_args = parser.parse_args(args)
    path = f"appliedCustomerBillingRate?billingAccount.id={parsed_args.billingaccount}&bill.id={parsed_args.bill}"
    a = cx.call(verb=Verb.GET, service=SRV_BILLING, path=path)
    if format == "json":
        print_json(json.dumps(a))
    else:
        acbrs_as_table(a)
