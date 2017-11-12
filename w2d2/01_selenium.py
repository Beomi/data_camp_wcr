from selenium import webdriver

# chromedriver의 경로를 지정해주세요.
driver = webdriver.Chrome('chromedriver')
driver.get('http://naver.com')
driver.quit()
