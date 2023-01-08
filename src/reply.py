import requests
import json 
from src.setting import API_KEY_FACEBOOK

API_KEY = API_KEY_FACEBOOK
url = f'https://graph.facebook.com/v14.0/me/messages?access_token={API_KEY}'
headers = {
        "Content-Type": "application/json"
    }

def responseMessenger(sender_id, text):

    datos = {
        "messaging_type": "RESPONSE",
        "recipient": {
        "id": sender_id
        },
        "message": {
            "text": text
        }
    }
    response = requests.post(url, data=json.dumps(datos), headers=headers)
    print(response.text)

def senderAction(sender_id):
    datos = {
            "recipient":{
            "id":sender_id
        },
        "sender_action":"typing_on"
    }
    response = requests.post(url, data=json.dumps(datos), headers=headers)