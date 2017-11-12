import requests
from bs4 import BeautifulSoup as bs
from dateutil import parser

# 사람들 > 인터뷰
r = requests.get('http://www.yonhapnews.co.kr/section/7311020001.html')  # 연합뉴스 사람들 > 인터뷰
r.encoding = 'utf-8'  # 인코딩을 강제로 넣어줘야 제대로 나옵니다.
soup = bs(r.text, 'lxml')

interview_list = soup.select('li.section02')

for i in interview_list:
    print('제목: ', i.select_one('a').text.strip())
    print('Lead: ', i.select_one('p.lead').text.strip())
    print('링크: ', i.select_one('a')['href'])
    print('시각: ', i.select_one('span.p-time').text.strip())
    # 시각을 python datetime객체로
    print('Py Datetime: ', parser.parse(i.select_one('span.p-time').text.strip()))

# 연예기사 전체기사
# r2 = requests.get('http://www.yonhapnews.co.kr/entertainment/1104000001.html')  # 연합뉴스 연예기사 전체
# r2.encoding = 'utf-8'  # 인코딩을 강제로 넣어줘야 제대로 나옵니다.
# soup = bs(r2.text, 'lxml')
#
# interview_list2 = soup.select('li.section02')
#
# for i2 in interview_list2:
#     print('제목: ', i2.select_one('a').text.strip())
#     print('Lead: ', i2.select_one('p.lead').text.strip())
#     print('링크: ', i2.select_one('a')['href'])
