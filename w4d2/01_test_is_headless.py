from selenium import webdriver

TEST_URL = 'http://localhost:8000/Chrome%20Headless%20Detection.htm'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--test-type")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("proxy-server=localhost:8080")
driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get(TEST_URL)

user_agent = driver.find_element_by_css_selector('#user-agent').text
plugins_length = driver.find_element_by_css_selector('#plugins-length').text
languages = driver.find_element_by_css_selector('#languages').text
webgl_vendor = driver.find_element_by_css_selector('#webgl-vendor').text
webgl_renderer = driver.find_element_by_css_selector('#webgl-renderer').text

print('User-Agent: ', user_agent)
print('Plugin length: ', plugins_length)
print('languages: ', languages)
print('WebGL Vendor: ', webgl_vendor)
print('WebGL Renderer: ', webgl_renderer)
driver.quit()
