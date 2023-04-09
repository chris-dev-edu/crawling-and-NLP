from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

def get_url_by_year(year):
    return "https://www.genie.co.kr/chart/musicHistory?year={}&category=0".format(year)

def get_song_info(driver, titles):
    song_links = driver.find_elements(by=By.CLASS_NAME, value="link")
    num_of_songs = len(song_links)

    for num in range(num_of_songs):
        link = driver.find_elements(by=By.CLASS_NAME, value="link")[num]
        link.find_element(by=By.TAG_NAME, value="a").click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        info = soup.select('.value')
        title = soup.select_one('.name').get_text().strip()
        singer = info[0].get_text().strip()
        play_time = info[3].get_text().strip()
        lyrics = soup.select_one('#pLyrics').select_one('p').get_text().strip()

        titles.append(title)

        driver.back()

all_title = {}

for year in range(1971, 1972):
    url = get_url_by_year(year)

    titles = []

    driver.get(url)
    get_song_info(driver, titles)

    song_links = driver.find_elements(by=By.CLASS_NAME, value="link")
    num_of_songs = len(song_links)

    if num_of_songs > 49:
        driver.find_element(by=By.CLASS_NAME, value='page-nav').find_elements(by=By.TAG_NAME, value='a')[1].click()
        get_song_info(driver, titles)

    all_title[year] = titles

print(all_title)
