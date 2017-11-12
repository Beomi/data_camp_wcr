import requests

with requests.Session() as s:
    dic = {
        'hello': 'world'
    }
    res = s.post('http://httpbin.org/post', data=dic)
    print(res.text)
