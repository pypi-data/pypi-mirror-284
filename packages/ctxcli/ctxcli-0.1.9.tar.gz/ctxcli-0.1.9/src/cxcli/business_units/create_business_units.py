import csv
from cxcli import USER_SERVICE_NAME, BUSINESS_UNIT_SERVICE_NAME
from cxcli.tools.api_utils.cx_caller import CxCaller, Verb
from cxcli.tools.common_utils import check_csv_mandatory_fields
from rich import print
from tqdm import tqdm
import pandas as pd

MANDATORY_FIELDS = ['name', 'businessUnitSpec.buType','businessUnitSpec.href']

    
def create_business_unit(cx: CxCaller,payload):
    add_user_response = cx.call(verb=Verb.POST, service=BUSINESS_UNIT_SERVICE_NAME, path=f"businessUnit", payload=payload,silent=True)
    return add_user_response

def process_row(cx: CxCaller, row, idx): 
    # if not check_csv_mandatory_fields(row, idx,MANDATORY_FIELDS):
    #     raise ValueError(msg)
                   
    spec_characteristics_names = row.get('speccharacteristics.names','')   
    spec_characteristics_values = row.get('speccharacteristics.values','')   
    spec_characteristics = []
    if spec_characteristics_names and spec_characteristics_values:            
        spec_characteristics_names_arr = spec_characteristics_names.split(",")
        spec_characteristics_values_arr = spec_characteristics_values.split(",")  
        if len(spec_characteristics_names_arr) > 0:    
            for char in spec_characteristics_names_arr:
                spec_characteristics.append({
                    "name": char,
                    "value": spec_characteristics_values_arr[spec_characteristics_names_arr.index(char)]
                })                
    
    payload = {
        "name": row.get('name','') ,
        "description": row.get('description',''),
        "externalId": row.get('externalid',''),
        "address": {
            "street1": row.get('address.street1',''),
        	"street2": row.get('address.street2', ''),
        	"city": row.get('address.city', '')  ,
        	"postCode": row.get('address.postcode', ''),
        	"stateOrProvince": row.get('address.stateorprovince', '') ,
        	"country": row.get('address.country', '')
        },
        "phone": row.get('phone',''),
        "businessUnitSpec": {
            "buType": row.get('businessunitspec.butype',''),
            "href": row.get('businessunitspec.href','')  
        },
        "specCharacteristics": spec_characteristics,        
        "childOf": {
            "id": row.get('childof.id',''),
            "href": row.get('childof.href','')
        }
    }   
    
    return create_business_unit(cx, payload)

def create_business_units(cx: CxCaller, file):
    csv_file_path = file
    
    print(f"Starting to process data from {csv_file_path}...")
    row_count = len(pd.read_csv(csv_file_path)) 
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as input:
        csvreader = csv.DictReader(input)
        csvreader.fieldnames = [field.lower() for field in csvreader.fieldnames]
        successful_count = 0
        unsuccessful_count = 0
        wrong_rows = []
        rows = enumerate(csvreader, start=2)
        
        for idx, row in tqdm(rows,total=row_count,desc="Processing rows",colour="green"):
            try:
                process_row(cx, row, idx)                
                successful_count += 1                    
            except Exception as ex:
                unsuccessful_count += 1
                wrong_rows.append({"idx":idx,"error": ex})                

        if successful_count > 0:          
            print(f"[green]{successful_count} business unit{'s' if successful_count > 1 else ''} have been added successfully.[/]")
        if unsuccessful_count > 0:
            print(f"[red]The {unsuccessful_count} business unit{'s' if unsuccessful_count > 1 else ''} below could not be added:[/]")  
            for row in wrong_rows:
                print(f"[red]On row #{row['idx']}: {row['error']}[/]")
            print("[red]Please recheck the data and retry.[/]") 
            
                  
