from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


browser.get("https://flight.naver.com/")
#가는날 선택
browser.find_element(By.CLASS_NAME,"tabContent_option___mYJO").click()
#날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/button').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/button').click()

browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/section/button[1]'))
    )
    element.click()
except Exception as e:
    print(f"오류 발생: {e}")
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/section/button[1]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/section/div/button[2]').click()

#항공권검색 클릭
try:
    element = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'searchBox_txt__jQZGF'))
    )
    element.click()
except Exception as e:
    print(f"오류 발생: {e}")


try:
    elem=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'domestic_Flight__8bR_b')))
    for i in elem:
        print(i.text)
        print()
except Exception as e:
    print(f"오류 발생: {e}")