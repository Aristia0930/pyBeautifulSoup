from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


browser.get("http://naver.com")
# elem = browser.find_element(By.CLASS_NAME,"link_service")
# elem= browser.find_element(By.ID,"query")
#By.TAG_NAME
 #elem.get_attribute("href")
#elem.click()
#browser.back()
#browser.forward() 
#browser.refresh()
#browser.quit()
#browser.close()
#elem.send_keys("나도코딩") 값 입력하기
#elem.send_keys(Keys.ENTER)  엔터 하기
#xpath로해보기
# elem=browser.find_element(By.xpath,"//*[@id="sform"]/fieldset/button")

#네이버 로그인해보기
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()
#로그인 아이디 input 가져오기
browser.find_element(By.ID,"id").send_keys("")
browser.find_element(By.CLASS_NAME,"input_pw").send_keys("%")
#로그인버튼 클릭
browser.find_element(By.ID,"log.login").click()
#브라우저 html 정보 출력
print(browser.page_source)
browser.quit()