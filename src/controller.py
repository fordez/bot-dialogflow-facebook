from src.dialogflow import sendDialogflow
from src.reply import responseMessenger

def controller(payload):
    
    match payload['message_type']:
        case 'text':
            ai = sendDialogflow(payload['message'], 12345)
            print(ai)
            responseMessenger(payload['sender_id'], ai['answer'])
