import requests

requests.packages.urllib3.disable_warnings()

headers = {
    'Origin': 'https://www.schoolinfo.go.kr',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,la;q=0.2,da;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_s0.do',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
  ('HG_CD', ''),
  ('SEARCH_KIND', ''),
  ('HG_JONGRYU_GB', ''),
  ('GS_HANGMOK_CD', ''),
  ('GS_HANGMOK_NM', ''),
  ('GU_GUN_CODE', ''),
  ('SIDO_CODE', '1100000000'),
  ('GUGUN_CODE', ''),
  ('SRC_HG_NM', ''),
]


# verify=False 는 SSL 인증 Fail 방지
r = requests.post('https://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_l0.do', headers=headers, data=data, verify=False)

# 가져오는 결과는 json 데이터
print(r.json())
