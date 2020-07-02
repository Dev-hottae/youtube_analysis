import pandas as pd


aa = [{'kind': 'youtube#searchResult', 'etag': 'hTkxNbneVGK5shU2d8KesAa3Vvg', 'id': {'kind': 'youtube#video', 'videoId': 'TgOu00Mf3kI'}}, {'kind': 'youtube#searchResult', 'etag': 'fCs-s_YieasafMzZXaPkZRaFXjk', 'id': {'kind': 'youtube#video', 'videoId': 'QYNwbZHmh8g'}}]

bb = {'kind': 'youtube#searchResult', 'etag': 'hTkxNbneVGK5shU2d8KesAa3Vvg', 'id': {'kind': 'youtube#video', 'videoId': 'TgOu00Mf3kI'}}
data = pd.DataFrame(bb['id'])

print(data)


