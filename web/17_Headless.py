import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# Headless 모드 추가
chrome_options.add_argument("--headless")  # Headless 옵션
chrome_options.add_argument("--disable-gpu")  # GPU 가속 사용 안 함
chrome_options.add_argument("--window-size=1920x1080")  # 크롬 창 크기 설정 (필수)
chrome_options.add_argument("--no-sandbox")  # 리눅스에서 권한 문제 해결
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=chrome_options)



url="https://play.google.com/store/movies?hl=ko&pli=1"
browser.get(url)



browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")



interval=2

prev_height=browser.execute_script("return document.body.scrollHeight")


while True:

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    curr_height=browser.execute_script("return document.body.scrollHeight")

    if prev_height== curr_height:
        break
    prev_height=curr_height

print("완료")
browser.get_screenshot_as_file("google.png")





soup=BeautifulSoup(browser.page_source,"lxml")

movies=soup.find_all("div",attrs={"class" : "hP61id"})

for movie in movies:
    title=movie.find("div",attrs={"class" : "Epkrse"}).get_text()
    print(title)