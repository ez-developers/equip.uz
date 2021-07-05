from telegram.ext import MessageFilter
from bot.utils._reqs import parser
from backend.settings import API_URL
from requests.auth import HTTPBasicAuth
import json

j = json.load(open("bot/assets/text.json", "r"))


class FilterButton(MessageFilter):
    def __init__(self, section_key: str):
        self.section_key = section_key

    def filter(self, message):
        return message.text in parser(API_URL=f"{API_URL + self.section_key}/",
                                      API_auth=HTTPBasicAuth("admin", "admin"),
                                      key="name")


filterCategories = FilterButton("categories")
filterProducts = FilterButton("products")
