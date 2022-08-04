from fastapi import FastAPI
from src.hook import api

bot = FastAPI()
bot.include_router(api)


   