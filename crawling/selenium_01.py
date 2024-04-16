from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pymysql
import pymysql.cursors

driver = webdriver.Chrome()

driver.get("https://comic.naver.com/index") 

time.sleep(2)

webtoonMenu = driver.find_element(by=By.XPATH, value='//*[@id="menu"]/li[2]/a')
webtoonMenu.click()

time.sleep(1)


webtoonDict = {
    "월": [],
    "화": [],
    "수": [],
    "목": [],
    "금": [],
    "토": [],
    "일": []
}

dayList = list(webtoonDict.keys())

for day in dayList:
    webtoonDayMenus = driver.find_elements(by=By.CSS_SELECTOR, value='.SubNavigationBar__link--PXX5B')
    for menu in webtoonDayMenus:
        if menu.text != day:
            continue

        menu.click()
        time.sleep(1)

        scrollTop = 0
        while True:
            driver.execute_script(f"window.scrollTo(0, {scrollTop})")
            
            scrollTop += 500
            time.sleep(0.2)
            if scrollTop > driver.execute_script("return document.body.scrollHeight"):
                break
    
    webtoonList = []
    webtoonItems = driver.find_elements(by=By.CSS_SELECTOR, value='.ContentList__content_list--q5KXY .item')
    for item in webtoonItems:
        title = item.find_element(by=By.CSS_SELECTOR, value='.ContentTitle__title--e3qXt .text').text
        author = item.find_element(by=By.CSS_SELECTOR, value='.ContentAuthor__author--CTAAP').text
        rating = item.find_element(by=By.CSS_SELECTOR, value='.Rating__star_area--dFzsb .text').text
        imgUrl = item.find_element(by=By.CSS_SELECTOR, value='.Poster__image--d9XTI').get_attribute(name="src")
        
        webtoon = {
            "title": title,
            "author" : author,
            "rating" : float(rating),
            "imgUrl" : imgUrl
        }
        webtoonList.append(webtoon)
    webtoonDict[day] = webtoonList

host = "mysql-db.cz6i24w6m9m3.ap-northeast-2.rds.amazonaws.com"
port = 3306
user = "aws"
password = "1q2w3e!!"
database = "webtoon_db"

connection = pymysql.connect(host=host , port=port, user=user, password=password, database=database)
cursur = connection.cursor()
sql = f'''
insert into 
    webtoon_tb
values
'''

webtoonsOfDay = list(webtoonDict.items())
for day, webtoons in webtoonsOfDay:
    for webtoon in webtoons:
        sql += f'(0, "{day}", "{webtoon["title"]}", "{webtoon["author"]}", "{webtoon["rating"]}", "{webtoon["imgUrl"]}"),' 
sql = sql[:len(sql) - 1]  

cursur.execute(sql)
connection.commit()