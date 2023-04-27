import pandas
import matplotlib.pyplot as plt
import numpy as np

songs_data = pandas.read_csv('music_chart.csv')

all_songs = {}
max_runtime_song = { 'song': None, 'runtime': 0 }
min_runtime_song = { 'song': None, 'runtime': 999999 }

for song in songs_data.values:
    [year, title, singer, time, lyrics] = song

    [minutes, seconds] = [int(t) for t in time.split(":")]
    run_time_to_seconds = 60 * minutes + seconds

    if run_time_to_seconds > max_runtime_song['runtime']:
        max_runtime_song = { 'song': song, 'runtime': run_time_to_seconds }
    if run_time_to_seconds < min_runtime_song['runtime']:
        min_runtime_song = {'song': song, 'runtime': run_time_to_seconds}

    if year not in all_songs:
        all_songs[year] = { "total": run_time_to_seconds, "count": 1 }
    else:
        prev_total = all_songs[year].get("total")
        prev_count = all_songs[year].get("count")
        all_songs[year].update({ "total": prev_total + run_time_to_seconds, "count": prev_count + 1 })

years = []
average_runtimes = []

for year_key in all_songs:
    total_seconds = all_songs[year_key]['total']
    count = all_songs[year_key]['count']
    average_runtime_to_seconds = total_seconds / count
    years.append('%02d' % (year_key % 100))
    average_runtimes.append(average_runtime_to_seconds)
    print(f'{year_key}: {average_runtime_to_seconds}')

print("가장 긴 노래", max_runtime_song['song'])
print("가장 짧은 노래", min_runtime_song['song'])

def draw_graph():
    x = np.arange(len(all_songs))

    plt.bar(x, average_runtimes)
    plt.xticks(x, years)
    plt.show()

draw_graph()
