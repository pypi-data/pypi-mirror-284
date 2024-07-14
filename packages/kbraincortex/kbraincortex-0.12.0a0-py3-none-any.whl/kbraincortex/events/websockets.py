import uuid
from kbraincortex.azure.cosmos import get_item, delete_item, query_cosmos_db, insert_records_into_container
from kbraincortex.microsoft.graph import get_user_groups
from kbraincortex.microsoft.msal import validate_credentials
from kbraincortex.exceptions.collection import SubscriptionAuthenticationError
from kbrainsdk.security.bearer import extract_claims

def subscribe_to_group(token:str, group_name:str, client_id:str, tenant_id:str, client_secret:str) -> str:    
    _, email = authenticate_to_group(token, group_name, client_id, tenant_id, client_secret)
    subscription_id = uuid.uuid4()
    insert_records_into_container("websockets", "subscriptions", {"subscription_id": subscription_id, "group_name": group_name, "client_id": client_id, "tenant_id": tenant_id, "email": email})
    return subscription_id, email
    
def authenticate_to_group(token:str, group_name:str, client_id:str, tenant_id:str, client_secret:str) -> str:
    claims = extract_claims(f"Bearer {token}")
    email = claims.get("unique_name")
    user_groups = get_user_groups(token, client_id, tenant_id, client_secret)
    websocket_group_record = get_item("websockets", "groups", group_name)
    for group in user_groups:
        if group in websocket_group_record.get('authorized_entra_groups'):
            return True, email
    
    raise SubscriptionAuthenticationError("User is not authorized for this websocket group.")

def authenticate_to_subscription(token:str, group_name:str, subscription_id:str, client_id:str, tenant_id:str, client_secret:str) -> str:
    _, email = authenticate_to_group(token, group_name, client_id, tenant_id, client_secret)
    subscription_record = get_item("websockets", "subscriptions", subscription_id)
    if len(subscription_record) < 1:
        raise SubscriptionAuthenticationError("Subscription not found. Either the subscription ID is incorrect or the subscription has expired.")
    if subscription_record.get("email") != email:
        raise SubscriptionAuthenticationError("User is not authorized to listen to this websocket subscription.")
    
    return True, email

def unsubscribe_to_group(token:str, group_name:str, subscription_id:str, client_id:str, tenant_id:str, client_secret:str) -> str:
    _, email = authenticate_to_subscription(token, group_name, subscription_id, client_id, tenant_id, client_secret)
    delete_item("websockets", "subscriptions", subscription_id)
    return email
    
def get_subscribers(group_name:str, client_id:str, tenant_id:str, client_secret:str) -> str:
    query = {
        "query": "SELECT * FROM c WHERE c.group_name = @group_name and c.client_id = @client_id and c.tenant_id=@tenant_id",
        "parameters": [
            {"name": "@group_name", "value": group_name},
            {"name": "@client_id", "value": client_id},
            {"name": "@tenant_id", "value": tenant_id}
        ]
    }
    subscriptions, _ = query_cosmos_db(query, "websockets", "subscriptions")
    return subscriptions