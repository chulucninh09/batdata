import json
import requests


def fetch(url, headers=None, params=None):
    data = requests.get(url, params=params, headers=headers).text
    return json.loads(data)

