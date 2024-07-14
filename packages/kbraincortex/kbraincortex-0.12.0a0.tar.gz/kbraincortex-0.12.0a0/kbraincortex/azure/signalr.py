from azure.signalr import SignalRServiceClient, SignalRMessage
from kbraincortex.common.configuration import SIGNALR_CONNECTION_STRING

def send_signalr_message(message:str, target:str, hub_name:str, group_name:str|None, connection_string:str=SIGNALR_CONNECTION_STRING):
    signalr_client = SignalRServiceClient(connection_string)
    signalr_message = SignalRMessage(
        target=target, 
        arguments=[message]
    )

    if group_name:
        signalr_client.send_to_group(hub_name=hub_name, group_name=group_name, message=signalr_message)
    else:
        signalr_client.send(hub_name=hub_name, message=signalr_message)

#create a signalr hub
def create_signalr_hub(hub_name:str):
    signalr_client = SignalRServiceClient(SIGNALR_CONNECTION_STRING)
    signalr_client.create_hub(hub_name)
