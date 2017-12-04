from selenium import webdriver
import requests
import re
import time
import json

keys = json.load(open('id.json'))
ID = keys['id']
PW = keys['pw']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('input[name="username"]').send_keys(ID)
driver.find_element_by_css_selector('input[name="password"]').send_keys(PW)
driver.find_element_by_css_selector('div > form > span > button').click()

# time.sleep(3)

images = driver.find_elements_by_css_selector(
    'article'
)

srcset="https://scontent-icn1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/23823607_254901395041256_5493679551483478016_n.jpg 640w,https://scontent-icn1-1.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/23823607_254901395041256_5493679551483478016_n.jpg 750w,https://scontent-icn1-1.cdninstagram.com/t51.2885-15/e35/23823607_254901395041256_5493679551483478016_n.jpg 1080w"

src_list = srcset.split(',')

for src in src_list:
    # src = https://scontent-icn1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/23823607_254901395041256_5493679551483478016_n.jpg 640w
    url, width = src.split(' ')
    print(url)


for i in images:
    uploader = i.find_element_by_css_selector('a')
    img = i.find_element_by_css_selector('img')

    url = img.get_attribute('src')
    print(url)
    if url:
        response = requests.get(url, stream=True)
        filename = re.findall("[^/]*$", url)[0]
        f = open(filename, "wb")
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

driver.quit()