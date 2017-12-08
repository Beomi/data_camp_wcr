from bs4 import BeautifulSoup as bs
import requests

headers = {
    'Origin': 'https://openhanafn.tritops.co.kr',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,da;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://openhanafn.tritops.co.kr/content.jsp?search_flag=&search_word=',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
  ('search_flag', 'search'),
  ('tab', ''),
  ('lang', 'ko'),
  ('x1', '126977273'),
  ('x2', '126993299'),
  ('y1', '37561499'),
  ('y2', '37569619'),
  ('seq_no', '886'),
  ('type', ''),
  ('map_x', ''),
  ('map_y', ''),
  ('poi_pg', '1'),
  ('poi_ps', '10'),
  ('poi_x', ''),
  ('poi_y', ''),
  ('search_type', '0'),
  ('search_word', ''),
  ('btn_search', '\uC81C\uCD9C'),
]

r = requests.post('https://openhanafn.tritops.co.kr/content.jsp', headers=headers, data=data)

soup = bs(r.text, 'lxml')

pb_list = soup.select('div.result_list')

print(len(pb_list)) # 779개 

