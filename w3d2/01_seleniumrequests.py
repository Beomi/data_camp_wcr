from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import json

keys = json.load(open('naver.json'))

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
        ID = keys['id']
        PW = keys['pw']
        cookie_jar = get_cookies(ID, PW)
        with requests.Session() as s:
            s.headers = {
                'accept-language': 'ko-KR,ko',
                'user-agent': USER_AGENT,
                'accept': '*/*',
            }
            for cookie in cookie_jar:
                print(cookie)
                s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
            res = s.get('http://cafe.naver.com/ArticleList.nhn?search.clubid=27436155&search.menuid=61&search.boardtype=L')
            soup = bs(res.text, 'lxml')
            article_list = soup.select('#main-area > div > table > tbody > tr > td.board-list > span > a')
            for article in article_list:
                print(article.text, article['href'])
                article_url = article['href']
                res2 = s.get(article_url)
                soup = bs(res2.text, 'lxml')
                title = soup.select_one('div.tit-box > div.fl > table > tbody > tr > td:nth-of-type(1) > span')
                content = soup.select_one('#tbody')

    except Exception as e:
        print(e)
