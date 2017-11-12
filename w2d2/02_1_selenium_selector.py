from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.kakaobank.com/')

# 하나만 찾기
title = driver.find_element_by_css_selector('div.intro_main > h3')
# 여러개 찾기
small_titles = driver.find_elements_by_css_selector('div.cont_txt > h3')

print(title.text)

for t in small_titles:
    print(t.text)

driver.quit()
