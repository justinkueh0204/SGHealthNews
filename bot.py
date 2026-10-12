# Dependencies:
# pip install requests
# pip install python-telegram-bot
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
from newscraper import message

automatedtext = "Hello"

TOKEN: Final = """redacted""" 
BOT_USERNAME: Final = "@SGHealthNewsBot"
BASE_URL: Final = "https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/"
BOT_CHECK: Final = "https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/getUpdates"
CHANNEL_ID: Final = """redacted""" 

print(message)
send_message = 'https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/sendMessage?chat_id=-1002129489446&text={}'.format(message)
print(send_message)
requests.get(send_message)
