import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 크롬 드라이버 사용
# driver = webdriver.Chrome()

# 엣지 드라이버 사용
driver = webdriver.Edge()

# 접속할 URL
url = "https://www.naver.com"

# 드라이버를 활용하여 URL에 접속
driver.get(url)

# class name이 nav_item인 element들을 찾아서 4번째 index의 element를 click
driver.find_elements(by=By.CLASS_NAME, value="nav_item")[4].click()

# class name이 category_list__bmz__인 element들을 찾아서 5번째 index의 element를 click
driver.find_elements(by=By.CLASS_NAME, value="category_list__bmz__")[5].click()

# category라는 변수에 class name이 category_category_list__3u_RA인 element를 찾아서 저장
category = driver.find_element(by=By.CLASS_NAME, value="category_category_list__3u_RA")

# category element 내에서 class name이 category_list__bmz__인 element들을 찾아서 2번째 index의 element를 click
category.find_elements(by=By.CLASS_NAME, value="category_list__bmz__")[2].click()

# 2초 대기
time.sleep(2)

# 드라이버 종료
driver.close()