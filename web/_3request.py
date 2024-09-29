import requests

# res=requests.get("http://google.com")
res=requests.get("https://nadocoding.tistory.com/")
print("응답코드",res.status_code) #200 이면정상

if res.status_code==requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다",res.status_code)

res.raise_for_status() #문제가 생기면 프로그램 종료시킨다.
print("웹스크래핑진행중")

print(len(res.text)) #텍스트 가져오기
# print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)