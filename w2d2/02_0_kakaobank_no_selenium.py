import requests
from bs4 import BeautifulSoup as bs


res = requests.get('https://www.kakaobank.com/')
html = res.text

soup = bs(html, 'lxml')

title = soup.select_one('div.intro_main > h3')

print(title)