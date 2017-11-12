from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')
driver.set_window_size(1920, 1080)

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main_phantomjs.png')
