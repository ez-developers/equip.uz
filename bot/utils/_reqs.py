import requests
from requests.auth import HTTPBasicAuth


def parser(API_URL: str, key: str, API_auth: HTTPBasicAuth = None) -> list:
    custom_list = []
    obj = requests.get(API_URL, auth=API_auth).json()

    for i in obj:
        custom_list.append(i[key])
    return custom_list
