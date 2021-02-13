from keys import *
import requests
from requests_jwt import JWTAuth
import json

URL = 'https://api.clashofclans.com/v1/'
CLAN_TAG = '%232YJ8Y9R89'


def get_war_info():
    path = 'clans/' + CLAN_TAG + '/currentwar'

    full_path = URL + path

    head = {'Authorization': 'Bearer {}'.format(API_TOKEN)}

    return requests.get(full_path, headers=head)


if __name__ == '__main__':

    res = get_war_info()

    d = res.json()
    # # Serializing json
    json_object = json.dumps(d, indent=4)

    with open("war_info.json", "w") as outfile:
        outfile.write(json_object)