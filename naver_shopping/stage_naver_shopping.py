from lib.naver_shopping.crawler import crawl
from lib.naver_shopping.parser import parse
import json

pageString = crawl('')
products = parse(pageString)
# print(products)
# print(len(products))

for product in products:
    print(product)


file = open("./products.json","w+")
file.write(json.dumps(products))