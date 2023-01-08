import os
from google.cloud import dialogflow
from src.setting import PROJECT_ID_GOOGLE, LANGUAGE_CODE_DIALOGFLOW

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'keybot.json'
PROJECT_ID = PROJECT_ID_GOOGLE
LANGUAGE_CODE = LANGUAGE_CODE_DIALOGFLOW

def sendDialogflow(text,SESSION_ID):
 
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)
    text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    intent = response.query_result.intent.display_name
    query = response.query_result.query_text
    answer = response.query_result.fulfillment_text
        
    return {
        "intent": intent,
        "query": query,
        "answer": answer,
    }
