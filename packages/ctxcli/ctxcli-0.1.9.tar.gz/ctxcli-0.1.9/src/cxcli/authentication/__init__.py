import argparse
from cxcli.tools.api_utils.cx_caller import ENVS, get_domain_name
from cxcli.authentication.auth import get_token_from_config, write_token_env_to_config
from cxcli.tools.api_utils.cx_token import get_token
from rich.console import Console
from rich import print

def auth_cmd():
    console = Console()
    env = ""
    tenant = ""
    u = ""
    p = ""
    while env not in ENVS:
        env = console.input(f"Please enter [bold yellow]enviroment[/] ({','.join(ENVS)}):")
    while tenant == "":
        tenant = console.input("Please enter [bold yellow]tenant[/]:")
    while u == "":
        u = console.input("Please enter [bold yellow]username[/]:")
    while p == "":
        p = console.input("Please enter [bold yellow]password[/]:",password=True)
    domain_name = get_domain_name(env)
    print("Authenticating...")
    try:
        access_token, refresh_token, expires_in = get_token(u, p, tenant, domain_name)
        write_token_env_to_config(access_token=access_token,env=env, tenant=tenant, refresh_token=refresh_token, expires_in=expires_in)
        print("[bold green]Success[/]. You can now run the CLI again with any command")
    except Exception as ex:
        print(f"[bold red]{str(ex)}[/]")
    
def authcheck_cmd():
    results = get_token_from_config()
    if results[1] is not None:
        print(f"[bold green]You're currently authenticated to {results[0]} on {results[2]}[/]")        
    # else:
    #     print("[bold red]Token is not valid[/]")