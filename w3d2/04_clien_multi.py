from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup as bs
import json


def crawler(link):
    r = requests.get(link)
    html = r.text
    soup = bs(html, 'lxml')
    article = {}
    try:
        article['title'] = soup.select_one('h3').text.strip()
        article['content'] = soup.select_one('article').text.strip()
        article['date'] = soup.select_one('div.post-time').text.strip()
        print(article)
        return article
    except Exception as e:
        print(e)


if __name__ == '__main__':
    list_all = json.load(open('clien_list.json', 'r'))
    pool = Pool(processes=4)
    result = pool.map(crawler, list_all)
    json.dump(result, open('clien_result.json', 'w+'))
