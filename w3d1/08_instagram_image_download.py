from selenium import webdriver
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('input[name="username"]').send_keys('')
driver.find_element_by_css_selector('input[name="password"]').send_keys('')
driver.find_element_by_css_selector('div > form > span > button').click()

images = driver.find_elements_by_css_selector('#mainFeed > div > div > div > article > div > div > div > div > img')

for i in images:
    url = i.get_attribute('src')
    print(url)
    if url:
        response = requests.get(url, stream=True)
        filename = re.findall("[^/]*$", url)[0]
        f = open(filename, "wb")
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
