from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver')

# 네이버 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#id').send_keys('')
driver.find_element_by_css_selector('#pw').send_keys('')
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()

def get_post_url_list():
    CAFE_NUM = 27436155 # 이 카페 넘버는 카페별로 다릅니다.
    MENU_ID = 44 # 이 메뉴 아이디는 카페 내 게시판별로 다릅니다.

    driver.get(f'http://cafe.naver.com/ArticleList.nhn?search.clubid={CAFE_NUM}&search.menuid={MENU_ID}')

    # iframe 내부로 이동 (driver가 보는 document의 위치 전환)
    # .frame안의 값은 Frame의 name값
    driver.switch_to.frame('cafe_main')
    # 게시판 내 게시글 가져오기
    post_url_list = []
    post_list = driver.find_elements_by_css_selector('.board-list')
    for post in post_list:
        url = post.find_element_by_css_selector('a').get_attribute("href")
        # print('글제목: ', post.text)
        # print('글링크: ', url)
        post_url_list.append(url)
    
    return post_url_list

post_url_list = get_post_url_list()

for url in post_url_list:
    driver.get(url)
    driver.switch_to.frame('cafe_main')
    # Selenium의 find_element_by_css_selector 에서는 nth-child를 쓸 수 있습니다.
    title = driver.find_element_by_css_selector('table > tbody > tr > td:nth-child(1) > span')
    content = driver.find_element_by_css_selector('#tbody')
    print(title.text)
    print(content.text)
    sleep(2)

driver.quit()
