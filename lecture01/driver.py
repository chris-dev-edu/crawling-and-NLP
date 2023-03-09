import time

from selenium import webdriver

# 크롬 드라이버 사용
# driver = webdriver.Chrome()

# 엣지 드라이버 사용
driver = webdriver.Edge()

# 접속할 URL
url = "https://www.naver.com"

# 드라이버를 활용하여 URL에 접속
driver.get(url)

# 2초 대기
time.sleep(2)

# 드라이버 종료
driver.close()