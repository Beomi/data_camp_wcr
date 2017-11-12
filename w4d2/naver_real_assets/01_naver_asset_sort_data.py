import requests

headers = {
    'Origin': 'http://goodauction.land.naver.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,la;q=0.2,da;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'http://goodauction.land.naver.com/auction/ca_list.php',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
  ('class1', ''),
  ('ju_price1', ''),
  ('ju_price2', ''),
  ('bi_price1', ''),
  ('bi_price2', ''),
  ('num1', ''),
  ('num2', ''),
  ('lawsup', '0'),
  ('lesson', '0'),
  ('next_biddate1', ''),
  ('next_biddate2', ''),
  ('state', '91'),
  ('b_count1', '0'),
  ('b_count2', '0'),
  ('b_area1', ''),
  ('b_area2', ''),
  ('special', '0'),
  ('e_area1', ''),
  ('e_area2', ''),
  ('si', '11'),
  ('gu', '0'),
  ('dong', '0'),
  ('apt_no', '0'),
  ('order', 'bi_price ASC'), # 핵심은 이부분! Order by 가 어떻게 바뀌는지 확인해보면 됩니다.
  ('start', ''), # 시작번호: 1페이지는 비어있고 2페이지는 30, 3페이지는 60.... 즉 (n-1)x30 의 값이 들어가 30개씩 받아옵니다.
  ('total_record_val', ''), # 2페이지부터는 전체 개수가 들어가있어요.
  ('detail_search', ''),
  ('detail_class', ''),
  ('recieveCode', ''),
]

# 위 order에서 나오는 경우
# ASC / DESC
# 조회수: view_count
# 매각기일: next_biddate
# 유찰횟수: b_count
# 최저입찰가: bi_price
# 감정가 순: ju_price
# 소재지 순: address
# 한칸 띄워쓰고 조건 ASC 이렇게 쓰면 잘 결과를 받아옵니다.

r = requests.post('http://goodauction.land.naver.com/auction/ax_list.php', headers=headers, data=data)

print(r.text)
