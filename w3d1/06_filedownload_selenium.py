from selenium import webdriver
import os, time

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
print(THIS_DIR)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": THIS_DIR,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://deepmind.com/documents/29/DeepMindLab.pdf')
while True:
    if os.path.isfile('DeepMindLab.pdf'):
        break
    else:
        time.sleep(3)
driver.quit()
