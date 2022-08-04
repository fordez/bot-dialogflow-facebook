from src.reply import responseMessenger
from src.gpt3 import gpt3

def handler(payload):
    match payload['message_type']:
        case 'text':
            print(payload)
            nlp = gpt3(payload['message'])
            responseMessenger(payload['sender_id'], nlp['choices'][0]['text'])
        case 'location':
            print(payload)
        case 'media':
            print(payload)
    