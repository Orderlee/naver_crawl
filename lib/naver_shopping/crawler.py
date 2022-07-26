import requests
from lib.naver_shopping.parser import parse

def crawl(pageNo):
    url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%9B%90%ED%94%BC%EC%8A%A4&pagingIndex={}&pagingSize=40&productSet=total&query=%EC%9B%90%ED%94%BC%EC%8A%A4&sort=rel&timestamp=&viewType=list'.format(pageNo)
    data = requests.get(url)
    #print(data.status_code, url)
    return data.content

totalProducts = []
for pageNo in range(1, 10+1):
    pageString = crawl(pageNo)
    products = parse(pageString)
    totalProducts += products
# pageString = crawl('원피스',4)
# products = parse(pageString)
# print(products)
# print(len(products))
