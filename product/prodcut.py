from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pymysql
import pymysql.cursors
import re
from datetime import datetime

driver = webdriver.Chrome()

driver.get("https://puppydog.co.kr/category/%EB%AF%B8%EC%9A%A9%EC%9A%A9%ED%92%88/53/") 

time.sleep(1)

scrollTop = 0
while True:
    driver.execute_script(f"window.scrollTo(0, {scrollTop})")
    
    scrollTop += 500
    time.sleep(0.2)
    if scrollTop > driver.execute_script("return document.body.scrollHeight"):
        break

productItems = driver.find_elements(by=By.CSS_SELECTOR, value='#sp--layout > div.sp__layout_contents > div.xans-product-container > div > div.xans-element-.xans-product.xans-product-listnormal > div > ul > li')

product_values = []
stock_values = []

product_id_counter = 501
for item in productItems:
    nameKor = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_title_247 > a > span').text 
    price_str = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_description_content > span:nth-child(1)').text
    price = int(re.sub("[^0-9]", "", price_str))
    imgUrl = item.find_element(by=By.CSS_SELECTOR, value='.sp__product_image > img').get_attribute(name="src")
    
    product_values.append((product_id_counter, nameKor, price, imgUrl))
    
    for category in range(1, 5):
        stock_values.append((0, product_id_counter, category, 0, datetime.now(), datetime.now()))
    
    product_id_counter += 1

host = "mysql-db.cin5nw0tb1i7.ap-northeast-2.rds.amazonaws.com"
port = 3306
user = "aws"
password = "1q2w3e4r!!"
database = "pet_db"

connection = pymysql.connect(host=host , port=port, user=user, password=password, database=database)
cursor = connection.cursor()

productSql = '''
    INSERT INTO product_tb 
    (product_id, user_id, product_name_kor, product_price, product_image_url, product_category_id, product_animal_category_id, product_board_content, create_date, update_date)
    VALUES
'''

stockSql = '''
    INSERT INTO product_stock_tb 
    (product_stock_id, product_id, product_size_category_id, product_stock_count, create_date, update_date)
    VALUES
'''

for product in product_values:
    productSql += f'({product[0]}, 0, "{product[1]}", {product[2]}, "{product[3]}", 4, 1, null, now(), now()),' 
productSql = productSql[:-1]  

for stock in stock_values:
    stockSql += f'({stock[0]}, {stock[1]}, {stock[2]}, {stock[3]}, "{stock[4]}", "{stock[5]}"),' 
stockSql = stockSql[:-1]  

cursor.execute(productSql)
cursor.execute(stockSql)
connection.commit()