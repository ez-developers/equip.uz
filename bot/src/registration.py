from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      error)
from telegram.ext import CallbackContext
from backend.settings import API_URL, API_AUTHENTICATION
from bot.utils.json_to_dict import json_to_dict
import logging
import requests

txt = json_to_dict('bot/assets/text.json')


class Registration:
    """ 
    Base class for registration
    """

    def is_private_chat(self, chat_id: int):
        if chat_id > 0:
            return True
        else:
            return False

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        if self.is_private_chat(chat_id):
            all_users = []
            user_objects = requests.get(API_URL + 'users/',
                                        auth=API_AUTHENTICATION).json()
            for i in user_objects:
                all_users.append(i["user_id"])
            if chat_id in all_users:
                user = requests.get(API_URL + f'users/{chat_id}',
                                    auth=API_AUTHENTICATION).json()
                print(user)
                update.effective_message.reply_text(
                    "User exists", reply_markup=ReplyKeyboardRemove())
            else:
                return True
        else:
            pass  # The bot is working in the group.

    def request_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "NAME"
        context.bot.send_message(chat_id,
                                 "Hi there! Amma bot for providing you with the best products ever\n\n WHAT IS YOUR NAME?")
        logging.info(
            f"User {chat_id} has been greeted and  requested name. Returning state {state}")
        return state

    def request_phone(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        logging.info(
            f"{chat_id} is being requested his phone number. Returning state: CONFIRMING_PHONE")
        context.bot.send_message(chat_id=chat_id,
                                 text=self.phone_text,
                                 reply_markup=ReplyKeyboardMarkup(self.phone_button,
                                                                  resize_keyboard=True),
                                 parse_mode='HTML')
        return "CONFIRMING_PHONE"
