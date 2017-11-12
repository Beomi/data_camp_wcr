import requests
from bs4 import BeautifulSoup
import os

import telegram

bot = telegram.Bot(token='Telegram:botToken')
chat_id = bot.getUpdates()[-1].message.chat.id
bot.sendMessage(chat_id=chat_id, text=chat_id)
