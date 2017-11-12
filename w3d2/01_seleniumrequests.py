from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

def get_cookies(user_id, user_pw):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("user-agent={}".format(USER_AGENT))
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get('https://nid.naver.com/nidlogin.login')
    driver.find_element_by_css_selector('#id').send_keys(user_id)
    driver.find_element_by_css_selector('#pw').send_keys(user_pw)
    driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
    cookie = driver.get_cookies()
    driver.quit()
    return cookie

if __name__ == '__main__':
    try:
        ID = input('ID: ')
        PW = input('PW: ')
        cookie_jar = get_cookies(ID, PW)
        with requests.Session() as s:
            s.headers = {
                'accept-language': 'ko-KR,ko',
                'user-agent': USER_AGENT,
                'accept': '*/*',
            }
            for cookie in cookie_jar:
                s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
            res = s.get('https://nid.naver.com/user2/help/myInfo.nhn?lang=ko_KR')
            soup = bs(res.text, 'html.parser')
            nickname = soup.select_one('dd.nic_desc')
            print(nickname.text)
    except Exception as e:
        print(e)
