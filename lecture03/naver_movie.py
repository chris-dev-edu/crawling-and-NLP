import time

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas

driver = webdriver.Edge()

url = 'https://movie.naver.com/movie/point/af/list.naver?&page='

comments = []
star_points = []

for i in range(1000):
    driver.get(url+str(i+1))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    reviews = soup.select('tr')
    reviews.pop(0)

    for review in reviews:
        texts = review.get_text(separator="<TEST##>", strip=True).split("<TEST##>")

        star_point = texts[3]
        comment = texts[4]

        star_points.append(star_point)
        comments.append(comment)

    time.sleep(1)

data_frame = pandas.DataFrame(comments, columns=['리뷰'])
data_frame['별점'] = star_points
data_frame.to_csv('naver_movie.csv', index=False)