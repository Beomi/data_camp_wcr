import requests
from bs4 import BeautifulSoup as bs

with requests.Session() as s:
    useragent = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    s.headers = useragent

    k = s.get('https://www.ppomppu.co.kr/zboard/login.php', headers=useragent)
    print(s.cookies)

    for cookie in k.cookies:
        print (cookie.name, cookie.value)

    s.get('https://www.ppomppu.co.kr/zboard/login.php')
    login = s.post('https://www.ppomppu.co.kr/zboard/login_check.php', data={
        's_url': '/',
        'user_id': 'idid',
        'password': 'pwpw',
        'auto_login': "1"
    })

    res = s.get('https://www.ppomppu.co.kr/myinfo/member_my_comment_list.php')
    if '마이페이지는 로그인 후' in res.text:
        print('로그인에 실패했습니다.')
    else:
        print('로그인성공!')
        print(res.text)
        