import csv
import cxcli.customers.customer_data as customer_data
from cxcli.tools.api_utils.cx_caller import CxCaller, Verb
from cxcli.tools.common_utils import check_csv_mandatory_fields
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich import print
from tqdm import tqdm
import traceback
import threading
import pandas as pd

# Initialize counters and lists for tracking results
successful_count = 0
unsuccessful_count = 0
wrong_rows = []
counter_lock = threading.Lock()

def handle_customer_data(cx: CxCaller, individual_id):
    # Handle orders
    orders = customer_data.handle_orders(cx, individual_id)
    if orders not in (0, None):  # Check if there's an error message
        return orders
    # Handle product inventory
    product_inventory = customer_data.handle_product_inventory(cx, individual_id)
    if product_inventory not in (0, None):  # Check if there's an error message
        return product_inventory
    # Handle resource inventory
    resource_inventory = customer_data.handle_resource_inventory(cx, individual_id)
    if resource_inventory not in (0, None):  # Check if there's an error message
        return resource_inventory
    # Handle payment subscription
    payment_subscription = customer_data.handle_payment_subscription(cx, individual_id)
    if payment_subscription != 0:  # Check if there's an error message
        return payment_subscription
    # Handle payment method
    payment_method = customer_data.handle_payment_method(cx, individual_id)
    if payment_method != 0:  # Check if there's an error message
        return payment_method
    # Delete billing account
    billing_account = customer_data.delete_billing_account(cx, individual_id)
    if billing_account != 0:  # Check if there's an error message
        return billing_account
    # Delete customer
    customer = customer_data.delete_customer(cx, individual_id)
    if customer != 0:
        return customer
    # Delete individual
    individual = customer_data.delete_individual(cx, individual_id)
    if individual != 0:
        return individual
    return 0 # All operations successful


def process_row(cx: CxCaller, index, individual_id, status):
    individual = customer_data.get_individual(cx, individual_id)
    
    if individual:
        current_status = customer_data.get_profile_status(cx, individual_id)
        if(current_status == status):
            result = handle_customer_data(cx, individual_id)
            return result
        elif (current_status == None):
            return 'Customer is not found'
        else:
            return f'Profile is not {status}'
    else:
        return 'Individual is not found'
            

def delete_customers_list(cx: CxCaller, file):
    global successful_count, unsuccessful_count, wrong_rows, counter_lock
    csv_file_path = file
    
    print(f"Starting to process data from {csv_file_path}...")
    row_count = len(pd.read_csv(csv_file_path))

    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as input:
        csvreader = csv.DictReader(input)
        csvreader.fieldnames = [field.lower() for field in csvreader.fieldnames]
        
        if 'individual_id' not in csvreader.fieldnames or 'status' not in csvreader.fieldnames:
            print('Invalid header. Ensure that your first row has valid column names: individual_id and status')
            exit()
            
        rows = enumerate(csvreader, start=2)
        
        with ThreadPoolExecutor(max_workers=8) as executor:
            #create a dictionary named ‘all_tasks’ with keys as the result of executing ‘executor.submit(delete_entities, row)’ and values as ‘row’ for each ‘row’ in "csvreader"
            #It iterates over each row in rows, submits the function, and associates the result with the original row
            all_tasks = {}
            
            for index, row in rows:
                individual_id = row.get('individual_id', '').strip()
                status = row.get('status', '').strip()
                
                if not individual_id or not status:
                    print(f'Skipping row {index}: row has empty values for individual_id and/or status')
                    continue
                
                # Submit the task to executor and store future object with original index and row
                future = executor.submit(process_row, cx, index, individual_id, status)
                all_tasks[future] = (index, row)
            
            with tqdm(total=row_count, desc="Processing rows", colour="green") as pbar:
                for future in as_completed(all_tasks):
                    index, handled_record = all_tasks[future]
                    try:
                        result = future.result()
                        if result == 0:
                            with counter_lock:
                                successful_count += 1
                        else:
                            with counter_lock:
                                unsuccessful_count += 1
                                wrong_rows.append({"idx": index, "individual_id": handled_record.get("individual_id", "Not Found"), "error": result})
                    except Exception as e:
                        tqdm.write(
                            f"Handled record {str(handled_record)} with error:"
                            + traceback.format_exc()
                        )
                        with counter_lock:
                            unsuccessful_count += 1
                            wrong_rows.append({"idx": index, "individual_id": handled_record.get("individual_id", "Not Found"),"error": str(e)})
                    finally:
                        # Update the progress bar
                        pbar.update(1)
            
            if successful_count > 0:          
                print(f"[green]{successful_count} customer{'s' if successful_count > 1 else ''} have been deleted successfully.[/]")
            if unsuccessful_count > 0:
                print(f"[red]{unsuccessful_count} customer{'s' if unsuccessful_count > 1 else ''} below could not be deleted:[/]")  
                for row in wrong_rows:
                    print(f"[red]On row #{row['idx']}: {row.get('error', '')}[/]")
                print("[red]Please recheck the data and retry.[/]")


def delete_customer(cx: CxCaller, individual_id, status):
    result = process_row(cx, None, individual_id, status)
    
    if result == 0:
        print(f"[green]Customer have been deleted successfully.[/]")
    else:
        print(f"[red]{result}")
        