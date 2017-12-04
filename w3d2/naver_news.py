import requests
from multiprocessing import Pool
import time

start_time = time.time()

def get_data(article):
    article_id = article['articleId']

    headers = {
        'Origin': 'http://newslibrary.naver.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,da;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'http://newslibrary.naver.com/viewer/index.nhn?articleId=1980120200099203014&officeId=00009&publishDate=1980-12-02&isPopular=0',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    params = (
        ('urlKey', 'articleDetail'),
        ('viewID', 'app_articleDetail'),
        ('requestID', '4'),
        ('target', 'viewer'),
    )

    data = [
        ('articleId', article_id),
        ('detailCode', '1001000001000000000001101100000000000000000'),
    ]

    res = requests.post('http://newslibrary.naver.com/api/article/detail/json', headers=headers, params=params,
                        data=data)
    return res.json()['result']['article']['title']

headers = {
    'Origin': 'http://newslibrary.naver.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,da;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'charset': 'utf-8',
    'Referer': 'http://newslibrary.naver.com/search/searchByKeyword.nhn',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
  ('keyword', '수능'),
  ('page', '1'),
  ('startDate', '1920-04-01'),
  ('endDate', '1999-12-31'),
  ('order', '00010'),
  ('detailCode', '11111000010000011100011011000100111100100101'),
  ('pageSize', '100'),
  ('officeId', ''),
  ('includeSectionId', ''),
]

res = requests.post('http://newslibrary.naver.com/api/search/article/json', headers=headers, data=data)

article_list = res.json()['result']['articles']['article'] # 1000개 리스트

pool = Pool(processes=8)

data = pool.map(get_data, article_list)

import json

json.dump(data, open('naver_titles.json', 'w+'))


print('Total Time: ', time.time() - start_time)
