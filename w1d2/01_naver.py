import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://naver.com')

html = req.text
soup = bs(html, 'lxml')

# 이렇게 전부 써줄 수도 있지만
# hotkeyword_list = soup.select(
#     '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword '
#     '> div.ah_roll > div.ah_roll_area > ul.ah_l '
#     '> li.ah_item > a.ah_a > span.ah_k'
# )

# 이것처럼 줄여 쓸 수도 있어요.
hotkeyword_list = soup.select(
    'div.ah_roll_area > ul.ah_l > li.ah_item > a.ah_a > span.ah_k'
)

for hotkeyword in hotkeyword_list:
    print(hotkeyword.text.strip())
