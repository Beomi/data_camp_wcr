import requests
from bs4 import BeautifulSoup as bs

headers = {
    'dnt': '1',
}

params = (
    ('query', '나만의 웹 크롤러 만들기'),
)

res = requests.get('https://search.naver.com/search.naver', headers=headers, params=params)
html = res.text

soup = bs(html, 'lxml')

links = soup.select('div.section a[target="_blank"]')

for link in links:
    print('제목: ', link.text)
    print('링크: ', link['href'])
