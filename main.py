
import requests
import pandas as pd
import numpy as np
import keys


class You:

    HOST = 'https://www.googleapis.com/youtube/v3/'
    def __init__(self):
        self.keys = keys.key
        pass

    # 검색어 보내면 리스트로 영상 정보 리턴
    def search_func(self, q, maxResults=50, pageToken=None):
        '''
        :param q: 요청 검색어
        :param maxResults: 한번에 가져오는 데이터 갯수
        :param pageToken: 다음페이지 정보
        :return:
        '''

        add_url = 'search'
        query = {
            'part': 'id',
            'key': self.keys,
            'q': q,
            "maxResults": maxResults,
            'pageToken': pageToken,
        }
        res = requests.get(url=You.HOST+add_url, params=query).json()

        return res

    # 검색어랑 요청갯수 보내면 리스트로 영상 Id 리턴 (요청갯수는 50개 단위로)
    def search_all(self, search, num):
        '''
        :param search: 검색어
        :param num: 요청갯수
        :return: [{'kind': 'youtube#video', 'videoId': 'TgOu00Mf3kI'}, {'kind': 'youtube#video', 'videoId': 'QYNwbZHmh8g'}, {'kind': 'youtube#channel', 'channelId': 'UC3SyT4_WLHzN7JmHQwKQZww'}] 형식
        '''
        data_set = []
        loop = num/50
        next_token = None
        for i in range(int(loop)):
            one_part = self.search_func(q=search, maxResults=50, pageToken=next_token)

            # 다음페이지 토큰
            next_token = one_part['nextPageToken']
            data_set.extend([k['id'] for k in one_part['items'] if k['id']['kind'] == 'youtube#video'])

        return data_set

    # Input = <Youtube Channel ID>, <Youtube Data API Key>
    # Output = Count of subscriber of Youtube Channel
    def get_gudok(self, channel_ID, key):
        # get Json info
        URL = 'https://www.googleapis.com/youtube/v3/channels?&part=statistics&id={}&key={}'.format(channel_ID, self.key)
        result = requests.get(URL)
        result = result.json()

        # print(result['items'])
        # print(result['items'][0]['statistics']['viewCount'])
        # print(result['items'][0]['statistics']['subscriberCount'])

        # extract 'subscriberCount' from Json info
        gudok = result['items'][0]['statistics']['subscriberCount']

        return gudok

    # Input = <Youtube Video ID>, <Youtube Data API Key>
    # Output = Count of view of Youtube Video
    def get_johyeah(self, video_ID, key):
        # get Json info
        URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&part=statistics&id={}&key={}'.format(video_ID, self.key)
        result = requests.get(URL)
        result = result.json()

        # print(result['items'])
        # print("조회수 : ", result['items'][0]['statistics']['viewCount'])
        # result['items'][0]['statistics']['likeCount']
        # result['items'][0]['statistics']['dislikeCount']
        # result['items'][0]['statistics']['commentCount']

        # extract 'viewCount' from Json info
        johyeah = result['items'][0]['statistics']['viewCount']

        return johyeah

y = You()
pp = y.search_all(search='IU', num=100)
print(pp)
print(len(pp))