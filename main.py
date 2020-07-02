
import requests

key = 'AIzaSyAd2Xc9Bthqajmv5xtGNIw-uDuo1dKDqf0'

class You:

    HOST = 'https://www.googleapis.com/youtube/v3/'
    def __init__(self):
        pass

    def search_func(self, q='IU'):
        add_url = 'search'
        query = {
            'part': 'snippet',
            'key': key,
            'q': q
        }
        res = requests.get(url=You.HOST+add_url, params=query)
        print(res.text)
        return res.text