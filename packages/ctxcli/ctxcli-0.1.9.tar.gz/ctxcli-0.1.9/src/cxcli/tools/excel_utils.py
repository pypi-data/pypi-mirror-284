import os
from openpyxl import Workbook
from rich import print

# from openpyxl.styles import Font, Border, Side, Alignment


def export_to_excel(rows,headers, file_name):
    wb = Workbook()
    ws = wb.active
    ws.append(headers)
   
    if rows:
        column_names = list(rows[0].keys())

        # for order in tqdm(rows,total=len(rows),desc="Generating your report...",colour="green"):
        for order in rows:
            row = [order[column] for column in column_names]
            ws.append(row)

    if not file_name.endswith('.xlsx'):
        file_name += '.xlsx'
    wb.save(file_name)
    # print("[bold green]Success[/]. You can now run the CLI again with any command")
    print(f'[bold green]The export to {os.path.abspath(file_name)} has been succesfully completed.[/]')
    # print(f'Orders exported to {file_name}')