import glob
import csv

filenames = glob.glob(r'Charts\regional*.csv')

print(filenames)

def parse_charts(files):
    song_dict = {}
    for current_chart in files:
        with open(current_chart, "r", encoding='utf-8') as chart:
            date = 18
            chart.readline()
            chart = csv.reader(chart)
            for song_data in chart:
                entry = f'09-18-{date}'
                if song_data[2] not in song_dict:
                    song_dict[song_data[2]] = {entry:song_data[8]}
                else:
                    song_dict[song_data[2]][entry] = song_data[8]
    date += 1
    return song_dict

print(parse_charts(filenames))