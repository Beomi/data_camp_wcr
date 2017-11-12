import requests
from bs4 import BeautifulSoup as bs

product_num = 12339756540
r = requests.get(f'http://shopping.naver.com/detail/detail.nhn?nv_mid={product_num}')

soup = bs(r.text, 'lxml')

result_list = soup.select('#_review_list > li')

for i in result_list:
    print('제목: ', i.select_one('p.subjcet').text.strip())
    print('리뷰내용: ', i.select_one('div.atc').text.strip())
    print('-' * 30)
