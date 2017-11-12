import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://naver.com/')
html = r.text
soup = bs(html, 'lxml')

title = soup.select('#PM_ID_serviceNavi > li:nth-of-type(4) > a > span.an_txt')[0]

print(title.text)
