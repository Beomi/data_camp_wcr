from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.kakaobank.com/')
html = driver.page_source

soup = bs(html, 'lxml')

title = soup.select_one('div.intro_main > h3')

print(title.text)

driver.quit()
