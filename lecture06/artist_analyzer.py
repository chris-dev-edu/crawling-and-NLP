import pandas

song_data = pandas.read_csv('music_chart.csv')

artist = {}

for song in song_data.values:
    [_, title, singer, _, _] = song

    if singer not in artist:
        artist[singer] = { 'count': 1, 'titles': [title] }
    else:
        prev_count = artist[singer].get('count')
        prev_titles = artist[singer].get('titles')
        prev_titles.append(title)
        artist[singer].update({ 'count': prev_count + 1, 'titles': prev_titles })

def sort_artist(artist):
    artist_to_list = []
    for key, value in artist.items():
        artist_item = { 'artist': key }
        artist_item.update(value)
        artist_to_list.append(artist_item)

    return sorted(artist_to_list, key=lambda x: (-x['count']))

sorted_artist = sort_artist(artist)

for data in sorted_artist[0:11]:
    print(data)