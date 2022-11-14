import requests
from pprint import pprint

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





if __name__ == '__main__':
    most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])