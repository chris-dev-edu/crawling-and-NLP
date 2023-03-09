import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 창 크기 조절
def window_size():
    # 최대화
    driver.maximize_window()

    time.sleep(2)

    # 최소화
    driver.minimize_window()

# 마우스 스크롤
def scroll():
    # (0, 500) 스크롤 좌표로 이동
    driver.execute_script("window.scrollTo(0, 500)")

    time.sleep(2)

    # (0, 0) 스크롤 좌표로 이동
    driver.execute_script("window.scrollTo(0, 0)")

# 마우스 클릭
def click():
    # class name이 btn_more인 element를 찾아서 click
    driver.find_element(by=By.CLASS_NAME, value="btn_more").click()

    time.sleep(2)

    # class name이 btn_more인 element를 찾아서 click
    driver.find_element(by=By.CLASS_NAME, value="btn_more").click()

# 키보드 입력
def send_keys():
    # input_text라는 변수에 id가 query인 element를 찾아서 저장
    input_text = driver.find_element(by=By.ID, value="query")

    # 해당 element에 "부산 날씨" 라는 text 입력
    input_text.send_keys("부산 날씨")

# 마우스 클릭 + 키보드 입력
def click_and_send_keys():
    # input_text라는 변수에 id가 query인 element를 찾아서 저장
    input_text = driver.find_element(by=By.ID, value="query")

    # 해당 element에 "부산 날씨" 라는 text 입력
    input_text.send_keys("부산 날씨")

    time.sleep(2)

    # id가 search_btn인 element를 찾아서 click
    driver.find_element(by=By.ID, value="search_btn").click()

# 로그인 시도하기
def login():
    # class name이 link_login인 element를 찾아서 click
    driver.find_element(by=By.CLASS_NAME, value="link_login").click()

    time.sleep(2)

    # input_id 변수에 id가 id인 element를 찾아서 저장
    input_id = driver.find_element(by=By.ID, value="id")

    # 해당 element에 "chris" 라는 text 입력
    input_id.send_keys("chris")

    # input_id 변수에 id가 pw인 element를 찾아서 저장
    input_pw = driver.find_element(by=By.ID, value="pw")

    # 해당 element에 "123123" 이라는 text 입력
    input_pw.send_keys("123123")

    time.sleep(2)

    # class name이 btn_text인 element를 찾아서 click
    driver.find_element(by=By.CLASS_NAME, value="btn_text").click()

# html page_source 확인하기
def page_source():
    html = driver.page_source
    print(html)


url = "https://www.naver.com/"

driver = webdriver.Edge()
driver.get(url)
time.sleep(2)

# Selenium 기능 실행
# window_size()
# scroll()
# click()
# send_keys()
# click_and_send_keys()
# login()
# page_source()

time.sleep(2)
driver.close()