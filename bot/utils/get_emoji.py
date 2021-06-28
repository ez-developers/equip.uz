import os
import json


class Emoji:

    def __init__(self, key=None):
        self.key = key

    def get(self, key=None):
        path = os.path.abspath('assets/emojis.json')
        x = json.load(open(path, 'r'))
        for key in x:
            print(key)

        print(self)
