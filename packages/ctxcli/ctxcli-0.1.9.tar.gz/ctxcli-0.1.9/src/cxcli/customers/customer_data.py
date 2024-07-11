from cxcli.tools.api_utils.cx_caller import CxCaller, Verb
from cxcli import (
    INDIVIDUAL_SERVICE_NAME,
    CUSTOMER_SERVICE_NAME,
    ORDER_SERVICE_NAME,
    PRODUCT_INVENTORY_SERVICE_NAME,
    RESOURCE_INVENTORY_SERVICE_NAME,
    PAYMENT_SUBSCRIPTION_SERVICE_NAME,
    PAYMENT_METHOD_SERVICE_NAME,
    ACCOUNT_SERVICE_NAME
)
from tqdm import tqdm


def get_profile_status(cx: CxCaller, individual_id):
    response = (cx.call(verb=Verb.GET,service=CUSTOMER_SERVICE_NAME,path="customer?engagedParty.id=" + individual_id))
 
    if response:
        response = response[0].get('status')
    else:
        response = None

    return response


def get_individual(cx: CxCaller, individual_id):
    try:
        response = cx.call(verb=Verb.GET, service=INDIVIDUAL_SERVICE_NAME, path=f"individual/{individual_id}", silent=True)
        return response if response else None
    except ValueError as ve:
        return None
    
    
def handle_orders(cx: CxCaller, individual_id):
    NON_FINAL_ORDER_STATUS = ['draft', 'acknowledged', 'pending', 'held', 'inProgress', 'assessingCancellation', 'pendingCancellation']
    limit = 999
    offset = 0
    fields = 'id,state'
    path=f'productOrder/?&limit={limit}&offset={offset}&relatedParty.id={individual_id}&fields={fields}'
    
    try:
        orders = cx.call(verb=Verb.GET, service=ORDER_SERVICE_NAME, path=path)
        
        if len(orders) == 0:
            return None
        else:
            for order in orders:
                if order.get('state') in NON_FINAL_ORDER_STATUS:
                    if (order.get('state') == 'inProgress'):
                        try:
                            held = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "held"}, silent=True)
                            cancelled = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling order {order['id']}: {e}"
                    elif (order.get('state') == 'held'):
                        try:
                            cancelled = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling order {order['id']}: {e}"
                    elif (order.get('state') == 'assessingCancellation'):
                        try:
                            pendingCancellation = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "pendingCancellation"}, silent=True)
                            cancelled = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling order {order['id']}: {e}"
                    elif (order.get('state') == 'pending'):
                        try:
                            cancelled = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling order {order['id']}: {e}"
                    elif (order.get('state') == 'draft'):
                        try:
                            cancelled = cx.call(verb=Verb.PATCH, service=ORDER_SERVICE_NAME, path=f'productOrder/{order["id"]}', payload = {"state": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling order {order['id']}: {e}"
            return 0
    except Exception as e:
        return f"Error fetching orders: {e}"
    

def handle_product_inventory(cx: CxCaller, individual_id):
    NON_FINAL_PI_STATUS = ['active', 'pendingActive', 'suspended', 'pendingTerminate']
    limit = 999
    offset = 0
    fields = 'id,status'
    path=f'product?limit={limit}&offset={offset}&relatedParty.id={individual_id}&fields={fields}'
    
    try:
        product_inventory = cx.call(verb=Verb.GET, service=PRODUCT_INVENTORY_SERVICE_NAME, path=path)
        if len(product_inventory) == 0:
            return None
        else:
            for pi in product_inventory:
                if pi.get('status') in NON_FINAL_PI_STATUS:
                    if (pi.get('status') == 'active'):
                        try:
                            terminated = cx.call(verb=Verb.PATCH, service=PRODUCT_INVENTORY_SERVICE_NAME, path=f'product/{pi["id"]}', payload = {"status": "terminated"}, silent=True)
                        except Exception as e:
                            return f"Error handling product inventory {pi['id']}: {e}"
                    if (pi.get('status') == 'pendingActive'):
                        try:
                            cancelled = cx.call(verb=Verb.PATCH, service=PRODUCT_INVENTORY_SERVICE_NAME, path=f'product/{pi["id"]}', payload = {"status": "cancelled"}, silent=True)
                        except Exception as e:
                            return f"Error handling product inventory {pi['id']}: {e}"
                    if (pi.get('status') == 'suspended'):
                        try:
                            active = cx.call(verb=Verb.PATCH, service=PRODUCT_INVENTORY_SERVICE_NAME, path=f'product/{pi["id"]}', payload = {"status": "active"}, silent=True)
                            terminated = cx.call(verb=Verb.PATCH, service=PRODUCT_INVENTORY_SERVICE_NAME, path=f'product/{pi["id"]}', payload = {"status": "terminated"}, silent=True)
                        except Exception as e:
                            return f"Error handling product inventory {pi['id']}: {e}"
                    if (pi.get('status') == 'pendingTerminate'):
                        try:
                            terminated = cx.call(verb=Verb.PATCH, service=PRODUCT_INVENTORY_SERVICE_NAME, path=f'product/{pi["id"]}', payload = {"status": "terminated"}, silent=True)
                        except Exception as e:
                            return f"Error handling product inventory {pi['id']}: {e}"
            return 0
    except Exception as e:
        return f"Error fetching product inventory: {e}"
    
    
def handle_resource_inventory(cx: CxCaller, individual_id):
    limit = 999
    offset = 0
    path=f'resource?limit={limit}&offset={offset}&relatedParty.id={individual_id}'

    try:
        resources = cx.call(verb=Verb.GET, service=RESOURCE_INVENTORY_SERVICE_NAME, path=path)
        
        if len(resources) == 0:
            return None
        else:
            for r in resources:
                resource_id = r.get('id')
                resource_type = r.get('@type')
                
                if resource_type == "MSISDN":
                    try:
                        available = cx.call(verb=Verb.PATCH, service=RESOURCE_INVENTORY_SERVICE_NAME, path=f'resource/{resource_id}', payload = {"relatedParty":[], "resourceStatus": "available"}, silent=True)
                    except Exception as e:
                        return f"Error handling MSISDN {resource_id}: {e}"
                if resource_type == "ICCID":
                    try:
                        resource_relationship = r.get("resourceRelationship")
                        imsi_item = [item for item in resource_relationship if item["resource"]["@type"] == "IMSI"]
                        payload = {"relatedParty":[], "resourceStatus": "terminated", "resourceRelationship": imsi_item}
                        terminated = cx.call(verb=Verb.PATCH, service=RESOURCE_INVENTORY_SERVICE_NAME, path=f'resource/{resource_id}', payload = payload, silent=True)
                    except Exception as e:
                        return f"Error handling ICCID {resource_id}: {e}"
                if resource_type == "IMSI":
                    try:
                        terminated = cx.call(verb=Verb.PATCH, service=RESOURCE_INVENTORY_SERVICE_NAME, path=f'resource/{resource_id}', payload = {"relatedParty":[], "resourceStatus": "terminated"}, silent=True)
                    except Exception as e:
                        return f"Error handling IMSI {resource_id}: {e}"
            return 0
    except Exception as e:
        return f"Error fetching product inventory: {e}"
    

def handle_payment_subscription(cx: CxCaller, individual_id):
    limit = 999
    offset = 0
    path=f'paymentSubscription?limit={limit}&offset={offset}&payer.id={individual_id}'
    
    try:
        subscriptions = cx.call(verb=Verb.GET, service=PAYMENT_SUBSCRIPTION_SERVICE_NAME, path=path)
        
        if len(subscriptions) == 0:
            return 0
        else:
            for p in subscriptions:
                psid = p.get("id")
                if (p.get('status') == 'ACTIVE'):
                    try:
                        inactivate = cx.call(verb=Verb.POST, service=PAYMENT_SUBSCRIPTION_SERVICE_NAME, path=f'paymentSubscription/{psid}/inactivate', silent=True)
                    except Exception as e:
                        return f"Error handling payment subscription {psid}: {e}"
            return 0
    except Exception as e:
        return f"Error fetching payment subscription: {e}"
    

def handle_payment_method(cx: CxCaller, individual_id):
    path=f'paymentMethod/?relatedParty.id={individual_id}'
    
    try:
        payment_methods = cx.call(verb=Verb.GET, service=PAYMENT_METHOD_SERVICE_NAME, path=path)
        
        if len(payment_methods) == 0:
            return 0
        else:
            for p in payment_methods:
                pmid = p.get("id")
                if p.get('status') == 'ACTIVE':
                    try:
                        inactivate = cx.call(verb=Verb.DELETE, service=PAYMENT_METHOD_SERVICE_NAME, path=f'paymentMethod/{pmid}', silent=True)
                    except Exception as e:
                        return f"Error inactivating payment method {pmid}: {e}"
            return 0
    except Exception as e:
        return f"Error retrieving payment methods for individual {individual_id}: {e}"
    
    
def delete_billing_account(cx: CxCaller, individual_id):
    path=f'billingAccount?relatedParty.id={individual_id}'
    
    try:
        billing_account = cx.call(verb=Verb.GET, service=ACCOUNT_SERVICE_NAME, path=path)
        
        if len(billing_account) == 0:
            return 'Billing Account is not found'
        else:
            account_id = billing_account[0].get("id")
            try:
                delete = cx.call(verb=Verb.DELETE, service=ACCOUNT_SERVICE_NAME, path=f'billingAccount/{account_id}', silent=True)
            except Exception as e:
                return f"Error deleting billing account {account_id}: {e}"
        return 0
    except Exception as e:
        return f"Error fetching billing account: {e}"
    

def delete_customer(cx: CxCaller, individual_id):
    path=f'customer?engagedParty.id={individual_id}'
    
    try:
        customer = cx.call(verb=Verb.GET, service=CUSTOMER_SERVICE_NAME, path=path)
        
        customer_id = customer[0].get("id")
        try:
            delete = cx.call(verb=Verb.DELETE, service=CUSTOMER_SERVICE_NAME, path=f'customer/{customer_id}', silent=True)
        except Exception as e:
            return f"Error deleting customer {customer_id}: {e}"
        return 0
    except Exception as e:
        return f"Error fetching customer: {e}"


def delete_individual(cx: CxCaller, individual_id):
    path=f'individual/{individual_id}'
    try:
        delete = cx.call(verb=Verb.DELETE, service=INDIVIDUAL_SERVICE_NAME, path=path, silent=True)
    except Exception as e:
        return f"Error deleting individual {individual_id}: {e}"
    return 0