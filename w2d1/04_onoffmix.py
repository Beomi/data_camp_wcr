import requests
from bs4 import BeautifulSoup as bs

with requests.Session() as s:
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    login = s.post('https://onoffmix.com/account/login', data={
        'email': 'userid@mail.com',
        'pw': 'mypassword1234',
        'proc': 'login'
    })
    html = s.get('http://onoffmix.com/account/event')
    soup = bs(html.text, 'lxml')
    event_list = soup.select('#eventListHolder > div > ul > li.title > a')
    for event in event_list:
        print(event.text)
