import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://daum.net')

html = req.text
soup = bs(html, 'lxml')

# 이렇게 전부 써줄 수도 있지만
# hotkeyword_list = soup.select(
#     '#mArticle > div.cmain_tmp > div.section_media > '
#     'div.hot_issue.issue_mini > div.hotissue_layer > '
#     'ol > li > div > div:nth-of-type(1) > span.txt_issue > a'
# )
#

# 이것처럼 줄여 쓸 수도 있어요.
hotkeyword_list = soup.select(
    'div.hotissue_layer > ol > li > div > '
    'div:nth-of-type(1) > span.txt_issue > a'
)

for hotkeyword in hotkeyword_list:
    print(hotkeyword.text.strip())
