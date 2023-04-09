from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas

driver = webdriver.Chrome()

data_year = []
data_title = []
data_artist = []
data_time = []
data_lyrics = []

for year in range(1970, 2023):
    for page in range(1, 3):
        url = f'https://www.genie.co.kr/chart/musicHistory?year={year}&category=0&pg={page}'

        if year < 1984 and page == 2:
            continue

        driver.get(url)

        song_link_list = driver.find_elements(by=By.CLASS_NAME, value="link")
        num_of_song = len(song_link_list)

        for i in range(num_of_song):
            song_link_list = driver.find_elements(by=By.CLASS_NAME, value="link")
            song_link_list[i].find_element(by=By.TAG_NAME, value="a").click()

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            title = soup.select_one('.name').get_text().strip()
            info = soup.select('.value')  # 0:artist, 1:album, 2:genre, 3:run_time
            artist = info[0].get_text().strip()
            genre = info[2].get_text().strip()
            run_time = info[3].get_text().strip()
            lyrics_check = soup.select_one('#pLyrics')

            if lyrics_check == None:
                driver.back()
                continue

            lyrics = soup.select_one('#pLyrics').select_one('p').get_text().strip()

            data_year.append(year)
            data_title.append(title)
            data_artist.append(artist)
            data_time.append(run_time)
            data_lyrics.append(lyrics)

            # 뒤로가기
            driver.back()

data_frame = pandas.DataFrame(data_year, columns=['year'])
data_frame['title'] = data_title
data_frame['artist'] = data_artist
data_frame['run_time'] = data_time
data_frame['lyrics'] = data_lyrics
data_frame.to_csv('music_chart.csv', index=False)