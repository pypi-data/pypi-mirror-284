from cxcli import ORDER_SERVICE_NAME
from cxcli.tools.api_utils.cx_caller import CxCaller, Verb
from cxcli.tools.common_utils import get_comma_separated_values
from cxcli.tools.date_utils import transform_dates
from cxcli.tools.excel_utils import export_to_excel
from rich import print


def get_orders(cx: CxCaller, start_date, end_date):
    all_orders = []
    limit = 999
    offset = 0
    fields = "id,orderDate,state,completionDate,productOrderItem.productOffering.name,productOrderItem.productOffering.id,channel.id"
    path=f"productorder?&limit={limit}&offset={offset}&orderDate.gte={start_date}&orderDate.lte={end_date}&fields={fields}"    

    orders = cx.call(verb=Verb.GET, service=ORDER_SERVICE_NAME, path=path)
    all_orders.extend(orders)

    return all_orders


def export_orders(cx: CxCaller, start_date, end_date, output):
    print(f"Exporting orders from {start_date} to {end_date}...")
    
    start_iso, end_iso = transform_dates(start_date, end_date)
    
    all_orders = get_orders(cx, start_iso, end_iso)
    headers = ["ID", "Created At","Channel IDs","PO IDs", "PO Names","State", "Completion Date"]
    rows = []
    for order in all_orders:
        row = {            
            "ID": order["id"],
            "Created At": order.get("orderDate",""),
            "Channel IDs": get_comma_separated_values(order["channel"],"id"),
            "PO IDs": get_comma_separated_values(order["productOrderItem"],"productOffering","id"),
            "PO Name": get_comma_separated_values(order["productOrderItem"],"productOffering","name"),
            "State": order["state"],
            "Completion Date": order.get("completionDate","")
        }
        rows.append(row)
    export_to_excel(rows, headers, output)
    