from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

# 네이버 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#id').send_keys('')
driver.find_element_by_css_selector('#pw').send_keys('')
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()

# 네이버 가입 카페 목록 가져오기
driver.get('http://section.cafe.naver.com/')
cafe_list = driver.find_elements_by_css_selector('div.list_content > p.tit > a')
for cafe in cafe_list:
    print(cafe.text)

driver.quit()
