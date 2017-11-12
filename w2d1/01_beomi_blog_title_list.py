import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://beomi.github.io/')

html = r.text
soup = bs(html, 'lxml')
title_list = soup.select('div.tab > ul > li > a.preview__link')

for title in title_list:
    print(title.text)
