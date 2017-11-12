import requests
from bs4 import BeautifulSoup as bs

# 핵심은 이게 POST로 날아간다는 것

headers = {
    'Origin': 'https://www.schoolinfo.go.kr',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,la;q=0.2,da;q=0.2',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.schoolinfo.go.kr/ei/ss/Pneiss_b01_s0.do',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
    ('HG_CD', 'B100000435'), # 이 값이 학교의 고유값 J100000837 : 평택고
    ('GS_HANGMOK_CD', ''),
]

r = requests.post('https://www.schoolinfo.go.kr/ei/ss/Pneiss_b01_s0.do', headers=headers, data=data, verify=False)

html = r.text
soup = bs(html, 'lxml')

content = soup.select_one('.HomeContents')

print(content.text)
