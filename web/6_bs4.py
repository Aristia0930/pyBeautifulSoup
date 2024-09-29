import requests
from bs4 import BeautifulSoup

url="https://page.kakao.com/menu/10010"

res=requests.get(url)

res.raise_for_status() # 문제있으면 프로그램 종료

soup=BeautifulSoup(res.text,"lxml") # 우리가 가저온 웹 텍스트값을 beautifulsoup 형식의 객체로 만듬

# print(soup.body.div.div)
# 속성 확인 attrs
# 값확인 a["href"]

# print(soup.find("div",attrs={"class":"jsx-3256825605 font-small1 line-clamp-2 break-all text-el-60"}))
#div 태그 해당하면서 클래스가 blind인것을 찾는다
#text="" 이걸 사용하면 텍스트가 이것인걸 찾을수 있다.
#태그는 없어도 문제없다.
# wName=soup.find("div",attrs={"class":"jsx-3256825605 font-small1 line-clamp-2 break-all text-el-60"})
# print(wName.get_text()) # 텍스트만 가져옴 

li=soup.find("li",attrs={"class":"jsx-1700228029 jsx-4160309492 list-child-item shrink-0"})
print(li.a.span)
print(li.next_sibling.a.span) #다음껄로 넘어가기  형제 관계
#부모
# print(li.parent)
print(li.find_next_sibling("li")) #다음꺼중에 li인것만 찾는다
print(li.find_next_siblings("li")) #다음꺼중에 li 형제들 모두다 가져옴