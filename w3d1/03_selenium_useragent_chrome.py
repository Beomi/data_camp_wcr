from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
# Example: Mobile Safari
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Mobile Safari/537.36")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://www.google.com/search?q=my+user+agent')
driver.implicitly_wait(3)
my_user_agent = driver.find_element_by_css_selector('.xpdopen').text
print(my_user_agent)
