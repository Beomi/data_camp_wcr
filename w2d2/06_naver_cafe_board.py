from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver')

# 네이버 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#id').send_keys('')
driver.find_element_by_css_selector('#pw').send_keys('')
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()

# 네이버 가입 카페 목록 가져오기
CAFE_NUM = 25814079
driver.get(f'http://cafe.naver.com/ArticleList.nhn?search.clubid={CAFE_NUM}')

# iframe 내부로 이동 (driver가 보는 document의 위치 전환)
# .frame안의 값은 Frame의 id값
driver.switch_to.frame('cafe_main')
# 게시판 내 게시글 가져오기
post_list = driver.find_elements_by_css_selector('.board-list')
for post in post_list:
    print(post.text)

driver.quit()
