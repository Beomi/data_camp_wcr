from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = DesiredCapabilities.PHANTOMJS
options["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Mobile Safari/537.36"

driver = webdriver.PhantomJS('phantomjs', desired_capabilities=options)

driver.get('https://www.google.com/search?q=my+user+agent')
driver.implicitly_wait(3)
driver.save_screenshot('phantomjs_ddd.png')
my_user_agent = driver.find_element_by_css_selector('.xpdopen').text
print(my_user_agent)
