import requests
import re
from bs4 import BeautifulSoup


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
for i in range(1,6):
    print("현재 페이지 :",i)
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)


    res=requests.get(url,headers=headers)
    res.raise_for_status()


    soup=BeautifulSoup(res.text,"lxml")
    items=soup.find_all("li",attrs={"class":re.compile("^search-product")})
    
    # print(1)
    for item in items:
        #r광고제품은 제거 
        ad_bage=item.find("span",attrs={"class":"ad-badge-text"})
        if ad_bage:
            print("광고상품제외")
            print("------------------------------------------------------------")
            continue

        
        name=item.find("div",attrs={"class":"name"}).get_text()
        price=item.find("strong",attrs={"class" : "price-value"}).get_text()
        if "삼성" in name:
            print("삼성상품제외")
            print("------------------------------------------------------------")
            continue
        link=item.find("a",attrs={"class":"search-product-link"})["href"]
        print(name)
        print(price)
        print(link)
        print("------------------------------------------------------------")
