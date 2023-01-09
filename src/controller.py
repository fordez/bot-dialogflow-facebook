from src.dialogflow import sendDialogflow
from src.reply import responseMessenger, senderAction

def controller(payload):
    
    match payload['message_type']:
        case 'text':
            senderAction(payload['sender_id'])
            ai = sendDialogflow(payload['message'], 12345)
            print(ai)
            
            responseMessenger(payload['sender_id'], ai['answer'])
