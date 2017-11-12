from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('input[name="username"]').send_keys('')
driver.find_element_by_css_selector('input[name="password"]').send_keys('')
driver.find_element_by_css_selector('div > form > span > button').click()

images = driver.find_elements_by_css_selector('#mainFeed > div > div > div > article > div > div > div > div > img')

url_list = []
for i in images:
    url_list.append(i.get_attribute('src'))

print(url_list)
driver.quit()
