import requests
from bs4 import BeautifulSoup as bs

headers = {
    'Origin': 'http://auction.realestate.daum.net',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,la;q=0.2,da;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'http://auction.realestate.daum.net/v15/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}

params = (
    ('addr1', '서울'),  # 제일큰 지역(서울 등)
    ('addr2', '서초구'),  # 중간지역 / 성동구
    ('addr3', '서초동'),
    ('yongdo', '99'),
    ('yongdo_detail', '99'),
    ('sort', '12D'), # 정렬방법
)

# 정렬방법
# 사건번호순: 01A / 01D  ASC / DESC
# 감정가순: 03 A D
# 최저가순: 04 A D
# 매각기일순: 13 A D
# 조회수순: 12 A D

r = requests.post('http://auction.realestate.daum.net/ajax/main_list.php', headers=headers, params=params)

soup = bs(r.text, 'lxml')

apts = soup.select('p.address')

for i in apts:
    print(i.text)
