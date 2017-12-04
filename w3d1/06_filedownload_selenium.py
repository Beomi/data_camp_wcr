from selenium import webdriver
import os, time, re

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
print(THIS_DIR)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": THIS_DIR,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True, # PDF를 브라우저에서 열지 않도록
})

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://search.naver.com/search.naver?query=deepmind+pdf')

url_element_list = driver.find_elements_by_css_selector('a[href$=".pdf"]')

print(url_element_list)

url_list = []

for url_element in url_element_list:
    url = url_element.get_attribute('href')
    url_list.append(url)

print(url_list)

for url in url_list:
    try:
        driver.get(url)
        print(url)
        filename = re.findall("[^/]*$", url)[0]
        while True:
            if os.path.isfile(filename):
                break
            else:
                time.sleep(3)
    except Exception as e:
        print(e)

driver.quit()
