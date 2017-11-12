import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://naver.com')
html = r.text
soup = bs(html, 'lxml')
h1 = soup.select('h1')
print(h1[0].text.strip())
