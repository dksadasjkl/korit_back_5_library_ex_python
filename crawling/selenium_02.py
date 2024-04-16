from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pymysql
import pymysql.cursors

driver = webdriver.Chrome()

driver.get("https://puppydog.co.kr/") 

time.sleep(1)

shopMenu = driver.find_elements(by=By.CSS_SELECTOR, value='sp--btn sp--currentlink sp--initialized-currentlink')
for shopMenu in shopMenuList:

    shopMenu.click()

time.sleep(1)


shopDict = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : [],
}

categoryList = list(shopDict.keys())

for category in categoryList:
    categoryMenus = driver.find_elements(by=By.CSS_SELECTOR, value='.sp--btn sp--currentlink sp--initialized-currentlink')
    for menu in categoryMenus:
        if menu.text != category:
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
    
    categorys = []
    categoryItems = driver.find_elements(by=By.CSS_SELECTOR, value='.ContentList__content_list--q5KXY .item')
    for item in categoryItems:
        title = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_title_247 .span').text
        price = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_description_content .span').text
        imgUrl = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_image').get_attribute(name="src")
        
        category = {
            "title": title,
            "author" : author,
            "rating" : float(rating),
            "imgUrl" : imgUrl
        }
        categorys.append(category)
    shopDict[category] = categorys
    print(shopDict)

# host = "mysql-db.cz6i24w6m9m3.ap-northeast-2.rds.amazonaws.com"
# port = 3306
# user = "aws"
# password = "1q2w3e!!"
# database = "webtoon_db"

# connection = pymysql.connect(host=host , port=port, user=user, password=password, database=database)
# cursur = connection.cursor()
# sql = f'''
# insert into 
#     webtoon_tb
# values
# '''

# webtoonsOfDay = list(webtoonDict.items())
# for day, webtoons in webtoonsOfDay:
#     for webtoon in webtoons:
#         sql += f'(0, "{day}", "{webtoon["title"]}", "{webtoon["author"]}", "{webtoon["rating"]}", "{webtoon["imgUrl"]}"),' 
# sql = sql[:len(sql) - 1]  

# cursur.execute(sql)
# connection.commit()