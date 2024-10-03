import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


url="https://play.google.com/store/movies?hl=ko&pli=1"
browser.get(url)
#스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)") #1920*1080 만큼 내린다.


#화면 가장 아래로 스크룰 내리기(페이지 높이 만큼 내리기)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# movies=soup.find_all("div",attrs={"class" : "hP61id"})

#무한히 스크룰 내리는 방법
interval=2
#현재 문서 높이 저장
prev_height=browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스쿨로 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    #현재 높이 다시 저장
    curr_height=browser.execute_script("return document.body.scrollHeight")

    if prev_height== curr_height:
        break
    prev_height=curr_height

print("완료")

# for movie in movies:
#     title=movie.find("div",attrs={"class" : "Epkrse"}).get_text()
#     print(title)


import requests
from bs4 import BeautifulSoup


soup=BeautifulSoup(browser.page_source,"lxml")

movies=soup.find_all("div",attrs={"class" : "hP61id"})



# with open("movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title=movie.find("div",attrs={"class" : "Epkrse"}).get_text()
    print(title)