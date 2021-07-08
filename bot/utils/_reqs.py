from requests.auth import HTTPBasicAuth
from backend.settings import API_URL
import requests
import dotenv
import os

dotenv.load_dotenv()
auth = (os.getenv('REST_API_USERNAME'),
        os.getenv('REST_API_PASSWORD'))


def parser(API_URL: str, key: str, API_auth: HTTPBasicAuth = None) -> list:
    custom_list = []
    obj = requests.get(API_URL, auth=API_auth).json()

    for i in obj:
        custom_list.append(i[key])
    return custom_list


def target_category_id(category_name: str) -> int:
    response = requests.get(API_URL + 'categories/',
                            auth=auth)
    for i in response.json():
        if i["name"] == category_name:
            return i["id"]


def products_list(category_id: int) -> list:
    output = []
    all_products = requests.get(API_URL + 'products/',
                                auth=auth).json()
    for i in all_products:
        if i['category'] == category_id:
            output.append(i['name'])
    return output


def product_details(product_name: str) -> dict:
    response = requests.get(API_URL + 'products/',
                            auth=auth).json()
    for product in response:
        if product['name'] == product_name:
            return product
