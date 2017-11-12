import requests
from bs4 import BeautifulSoup as bs
import json

list_all = []
BASE_URL = 'https://www.clien.net'

for PAGE_NUM in range(15):
    res = requests.get(f'{BASE_URL}/service/group/clien_all?&od=T31&po={PAGE_NUM}')
    html = res.text
    soup = bs(html, 'lxml')
    links = soup.select('#div_content > div.card-grid > div > div > div > div.list-title > a')
    for l in links:
        list_all.append(BASE_URL + l['href'])

json.dump(list_all, open('clien_list.json', 'w+'))
