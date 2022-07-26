from bs4 import BeautifulSoup

def getProductInfo(li):
    #print(li)
    img = li.find('img')
    alt=img['alt']
    print(alt)
    price = li.find("span",{'class':"price_num__2WUXn"})
    # print(price)
    aTit = li.find("a",{"class":"basicList_link__1MaTN"})
    href=aTit['href']
    #print(href)
    return {"name":alt,"price":price.text.replace(",","").replace("원",""),"link":href}



def parse(pageString):

    bsObj = BeautifulSoup(pageString, 'html.parser')
    ul = bsObj.find("ul",{'class':'list_basis'})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})
    #print(len(lis))
    #print(lis[0])

    products = []
    for li in lis[:1]:
        product = getProductInfo(li)
        products.append(product)

    return products