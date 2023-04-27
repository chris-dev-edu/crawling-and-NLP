import pandas
from collections import Counter

song_data = pandas.read_csv('music_chart.csv')

words = []
filter_words = ['내가', '나를', '너를', '나의', '너의', '나는', '그대', '내게', '우리', '니가', '네가', 'me', 'my', 'you']

def word_filter(x):
    return len(x) > 1 and x not in filter_words

for song in song_data.values:
    [_, _, _, _, lyrics] = song

    if type(lyrics) == str:
        lyrics.replace('\n', '')
        words.extend(filter(word_filter, lyrics.split()))

counter = Counter(words)

for word, count in counter.most_common(20):
    print(f'{word}: {count}')
