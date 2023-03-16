import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

"""
def getUrlByPage(page):
    return "https://movie.naver.com/movie/point/af/list.naver?&page="+str(page)

for i in range(10):
    driver.get(getUrlByPage(i+1))
    time.sleep(2)
"""

url = "https://movie.naver.com/movie/point/af/list.naver?&page=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.findAll('tbody')[0].findAll('tr')

for review in reviews:
    information = review.findAll('td')
    print('번호: ', information[0].get_text())
    print('리뷰: ', information[1].find('em').get_text())
    print('평점: ', information[1].get_text())