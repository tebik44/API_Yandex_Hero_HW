import requests
from pprint import pprint
import os

# Задание 1 --->
def most_intelligence_hero(names):
    stats_hero = {}
    for surname in names:
        resp_uri = requests.get('https://www.superheroapi.com/api/2619421814940190/search/' + surname)
        dict_ = resp_uri.json()
        stats_hero[dict_['results'][0]['name']] = int(dict_['results'][0]['powerstats']['intelligence'])

    for key, value in stats_hero.items():
        print(f"{key} с интелектом {value}")

    print(f"Самый умный является {list(stats_hero.keys())[list(stats_hero.values()).index(max(stats_hero.values()))]} c интеллектом - {max(stats_hero.values())}")


# Задание 2 --->
class YaUploader:

    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers_authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        uri = 'v1/disk/resources/files/'
        request_url = self.base_host + uri
        params = {'limit': 2}
        response = requests.get(request_url, headers=self.get_headers_authorization(), params=params)
        print(response.json())

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path}
        response = requests.get(request_url, headers=self.get_headers_authorization(), params=params)
        print('Статус запроса - ', response.status_code)
        pprint(response.json())
        return response.json()['href']

    def POST_upload_local_file_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers_authorization())
        if response.status_code == 201:
            print('\nЗагрузка произошла успешно!')



if __name__ == '__main__':
    # most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])
    path_to_file = 'cats.png'
    token = 'y0_AgAAAAArqShkAADLWwAAAADUCEKCV9gR-WOAQA2ZoKwhzwNuUu_qyEk'
    uploader = YaUploader(token)
    uploader.POST_upload_local_file_to_disk(path_to_file, '/first_test.png')

