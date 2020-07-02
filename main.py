
import requests
import pandas as pd
import numpy as np
import keys


class You:

    HOST = 'https://www.googleapis.com/youtube/v3/'
    def __init__(self):
        self.keys = keys.key
        pass

    def search_func(self, q, maxResults=5, pageToken=None):
        add_url = 'search'
        query = {
            'part': 'id',
            'key': self.keys,
            'q': q,
            "maxResults": maxResults,
            'pageToken':pageToken,
        }
        res = requests.get(url=You.HOST+add_url, params=query).json()

        return res

    def search_all(self, search, num):
        data_set = pd.DataFrame(columns=['kind', 'videoId'])
        # data_set = []
        loop = num/50
        next_token = None
        for i in range(int(loop)):
            one_part = self.search_func(q=search, maxResults=50, pageToken=next_token)
            print(one_part)
            print(one_part['items'])
            # return
            # print(one_part['items'])
            print("end onepart")
            for_id = pd.DataFrame(one_part['items']).id
            data_set.append(for_id)
            # print(data_set)
            next_token = one_part['nextPageToken']

        return data_set




y = You()
pp = y.search_func('IU', maxResults=5, pageToken=None)
print(pp)
# datas = y.search_all(search="IU", num=100)
# pd_datas = pd.DataFrame(datas)
# print(datas)
# print(len(datas))
# print("---------------------------------------")
# print(datas2)

refine_datas = {}