import requests
from bs4 import BeautifulSoup

res=requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
count=1
spans = soup.find_all('span', class_='thumb-image')
imgs= [span.find('img')['src'] for span in spans if span.find('img')]
for img_url in imgs:
    print(img_url)
    img_res=requests.get(img_url)
    img_res.raise_for_status()
    with open(f"move{count}.jpg","wb") as f:
        f.write(img_res.content)
    count+=1