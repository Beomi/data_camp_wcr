import requests
from bs4 import BeautifulSoup as bs


r = requests.get('https://www.commoncriteriaportal.org/products/')
soup = bs(r.text, 'lxml')

product_list = soup.select('tbody > tr')

print(len(product_list)) # 2314

for product in product_list[:20]:
    product_name = product.select('td')[0]
    print(product_name.text.split('\n')[1].strip())