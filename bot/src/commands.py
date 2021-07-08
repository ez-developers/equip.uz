from telegram.ext import CallbackContext
from telegram import Update
from backend.settings import API_URL
from bot.utils._reqs import auth
import requests
import os
import dotenv


class Command:

    def __init__(self):
        pass

    def is_private_chat(self, chat_id: int):
        if chat_id > 0:
            return True
        else:
            return False

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        if chat_id > 0:
            all_users = []
            user_objects = requests.get(API_URL + 'users/',
                                        auth=auth).json()
            for i in user_objects:
                all_users.append(i["user_id"])
            if chat_id in all_users:
                print("User exists")
            else:
                self.request_name(update, context)
                print("TAKE ME TO THE REGISTRATION!!!")
        else:
            pass  # The bot is working in the group.

    def help_command(self, update: Update, context: CallbackContext):
        print(self, 'help', update.effective_chat.id)

    def menu(self):
        print(self, 'menu')

    def reset(self):
        print(self, 'reset')
