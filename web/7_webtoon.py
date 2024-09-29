import requests
from bs4 import BeautifulSoup

url="https://page.kakao.com/content/58095657"

res=requests.get(url)

res.raise_for_status() # 문제있으면 프로그램 종료

soup=BeautifulSoup(res.text,"lxml") # 우리가 가저온 웹 텍스트값을 beautifulsoup 형식의 객체로 만듬
# cartonns=soup.find_all("div",attrs={"class":"relative rounded-8pxr overflow-hidden w-full h-full"})

# for name in cartonns:
#     print(name["aria-label"])
cartonns=soup.find_all("span",attrs={"class":"font-medium2 inline-flex shrink-0 grow text-el-60"})
print(soup.body)

for cartoon in cartonns :
    title = cartonns.a.get_text()
    link="~~"+cartoon.a["href"]