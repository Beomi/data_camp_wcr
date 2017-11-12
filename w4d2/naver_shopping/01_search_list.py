import requests
from bs4 import BeautifulSoup as bs

search_word = 'ds718'
r = requests.get(f'http://shopping.naver.com/search/all.nhn?query={search_word}')

soup = bs(r.text, 'lxml')

result_list = soup.select('div.info')

for i in result_list:
    print('제목: ', i.select_one('a.tit').text.strip())
    print('링크: ', i.select_one('a.tit')['href'])
    print('가격: ', i.select_one('span.num').text.strip(), '원')
    print('-' * 30)
