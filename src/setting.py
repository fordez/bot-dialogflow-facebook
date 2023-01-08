import os
from dotenv import load_dotenv

load_dotenv()

VERYFY_TOKEN_FACEBOOK = os.getenv("VERYFY_TOKEN_FACEBOOK")
API_KEY_FACEBOOK = os.getenv("API_KEY_FACEBOOK")

PROJECT_ID_GOOGLE = os.getenv("PROJECT_ID_GOOGLE")
LANGUAGE_CODE_DIALOGFLOW = os.getenv("LANGUAGE_CODE_DIALOGFLOW")