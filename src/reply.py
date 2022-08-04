import requests
import json 
from src.setting import API_KEY_FACEBOOK

API_KEY = API_KEY_FACEBOOK

def responseMessenger(sender_id, text):
    url = f'https://graph.facebook.com/v14.0/me/messages?access_token={API_KEY}'
    headers = {
        "Content-Type": "application/json"
    }
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

