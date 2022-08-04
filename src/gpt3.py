import openai
from src.setting import ORGANIZATION_OPENAI, API_KEY_OPENAI, MODELO_GPT3

openai.organization = ORGANIZATION_OPENAI
openai.api_key = API_KEY_OPENAI
modelo_gpt3 = MODELO_GPT3

def gpt3(promt):
    return openai.Completion.create(
                model=modelo_gpt3,
                prompt=promt,
                max_tokens=256,
                temperature=0
            )
    