import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://www.fastcampus.co.kr/category_data_camp/')

html = req.text
soup = bs(html, 'lxml')

# 이렇게 전부 써줄 수도 있지만
# lecture_list = soup.select(
#     '#page-section-6 > div.page-section-content.vc_row-fluid.mk-grid > '
#     'div.mk-padding-wrapper > div > div > '
#     'div > div > div > div > '
#     'div.padding_box > p.line_3'
# )

# 이것처럼 줄여 쓸 수도 있어요.
lecture_list = soup.select(
    'div.padding_box > p.line_3'
)

for lecture in lecture_list:
    # 엔터 태그(br)은 '\n'으로 나옵니다.
    # 따라서 .replace()를 통해 스페이스 하나로 바꿔줍니다.
    print(lecture.text.replace('\n',' ').strip())
