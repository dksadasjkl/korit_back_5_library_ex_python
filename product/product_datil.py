from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pymysql
import pymysql.cursors
import re
from datetime import datetime

driver = webdriver.Chrome()



# 방문한 페이지의 URL을 추적하기 위한 집합

visited_pages = set()

# 첫 번째 페이지로 이동
driver.get("https://puppydog.co.kr/category/%EC%82%AC%EB%A3%8C/49/") 

# 반복해서 사진을 가져올 요소의 클래스
class_name = "sp__product_box_247"

# 페이지를 반복해서 클릭하고 사진을 가져옴
while True:
    # 현재 페이지의 URL을 가져옴
    current_url = driver.current_url
    
    # 현재 페이지의 URL이 이미 방문한 페이지인 경우, 무한 루프를 방지하기 위해 종료
    if current_url in visited_pages:
        break
    
    # 이미 방문한 페이지로 표시
    visited_pages.add(current_url)

    # 해당 클래스의 요소들을 찾음
    elements = driver.find_element(by=By.CSS_SELECTOR, value='.sp__product_detail_contents > center > img').get_attribute(name="src")
    
    # 요소가 더 이상 없으면 반복문 종료
    if not elements:
        break
    
    # 각 요소를 클릭하고 페이지에서 사진을 가져오기
    for element in elements:
        # 요소 클릭
        element.click()
        time.sleep(2)  # 페이지가 로드될 때까지 대기
        
        # 여기에 사진을 가져오는 코드를 추가
        # 예를 들어, 사진을 가져오는 CSS 선택자를 사용하여 사진 요소를 찾고 이미지 URL을 가져올 수 있습니다.
        # 사진을 가져온 후에는 적절한 처리를 수행합니다.
        
        # 뒤로가기
        driver.back()
        time.sleep(2)  # 뒤로가기가 완료될 때까지 대기

# 작업이 끝나면 브라우저를 종료
driver.quit()
