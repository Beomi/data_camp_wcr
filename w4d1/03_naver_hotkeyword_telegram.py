import requests
from bs4 import BeautifulSoup as bs
import os
import json

import telegram

bot = telegram.Bot(token='Telegram:botToken')

req = requests.get('http://naver.com')

html = req.text
soup = bs(html, 'lxml')

hotkeyword_list = soup.select(
    'div.ah_roll_area > ul.ah_l '
    '> li.ah_item > a.ah_a > span.ah_k'
)

if os.path.exists('naver.json'):
    before_list = json.load(open('naver.json'))
else:
    before_list = []

striped_list = []

for hotkeyword in hotkeyword_list:
    striped_list.append(hotkeyword.text.strip())

if striped_list != before_list:
    json.dump(striped_list, open('naver.json', 'w+'))
    bot.sendMessage(chat_id=chat_id, text=striped_list[0])
