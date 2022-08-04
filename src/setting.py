import os
from dotenv import load_dotenv

load_dotenv()

ORGANIZATION_OPENAI = os.getenv("ORGANIZATION_OPENAI")
API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
VERYFY_TOKEN_FACEBOOK = os.getenv("VERYFY_TOKEN_FACEBOOK")
API_KEY_FACEBOOK = os.getenv("API_KEY_FACEBOOK")
MODELO_GPT3 = "text-davinci-002"