import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'userId': 'myidid',
    'userPassword': 'mypassword123'
}

with requests.Session() as s:
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.select_one('input[name="_csrf"]')
    print(csrf['value'])

    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
    print(LOGIN_INFO)

    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    print(login_req.status_code)
    
