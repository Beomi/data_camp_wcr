from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

# 페이스북 로그인 페이지
driver.get('https://www.facebook.com/login')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#email').send_keys('')
driver.find_element_by_css_selector('#pass').send_keys('')
driver.find_element_by_css_selector('#loginbutton').click()

# 크로링하기 쉬운 모바일 페이지로 넘어가기
driver.get('https://m.facebook.com/')

# Scroll 내리기
for _ in range(3):
    time.sleep(3)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 화면에 뜨는 모든 포스트 찾기
post_list = driver.find_elements_by_css_selector('section.storyStream > div')
for post in post_list:
    content_list = post.find_element_by_css_selector('div').get_attribute("innerText")
    print('----')
    print(content_list.strip())

driver.quit()
