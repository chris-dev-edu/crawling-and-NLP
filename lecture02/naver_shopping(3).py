import time

from bs4 import BeautifulSoup
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

for i in range(10):
    print('page <'+str(i+1)+'>')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select('.basicList_info_area__TWvzp')

    for item in list:
        title = item.select('.basicList_link__JLQJf')[0].get_text()
        price = int(item.select('.price_num__S2p_v')[0].get_text().replace(',', '').replace('원', ''))
        delivery_element = item.select('.price_delivery__yw_We')

        delivery = 0
        if len(delivery_element) != 0 :
            delivery = int('0' + item.select('.price_delivery__yw_We')[0].get_text().replace(',', '').replace('원', '').replace('배송비', '').replace('무료', ''))
        else:
            delivery = '배송비 정보 가져올 수 없음'

        result = 0
        if type(delivery) is int:
            result = title + str(price + delivery)
        else:
            result = title + str(price) + '(' + delivery +')'

        print(result)

    driver.find_element(by=By.CLASS_NAME, value="pagination_next__pZuC6").click()
    time.sleep(2)

# 2초 대기
time.sleep(2)

# 드라이버 종료
driver.close()