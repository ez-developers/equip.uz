from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext
from bot.utils.build_menu import build_menu
from bot.utils._reqs import parser
from backend.settings import API_URL
from requests.auth import HTTPBasicAuth
import logging
import json
import dotenv
import os
import requests


j = json.load(open("bot/assets/text.json", "r"))
text = j["texts"]
button = j["buttons"]["menu"]

dotenv.load_dotenv()
api_auth = HTTPBasicAuth(os.getenv("REST_API_USERNAME"),
                         os.getenv("REST_API_PASSWORD"))


class Menu:
    def __init__(self):
        self.menu_buttons = [
            [KeyboardButton(button["order"])],
            [KeyboardButton(button["contact"]),
             KeyboardButton(button["promo"])],
            [KeyboardButton(button["settings"])]
        ]

    def display(self, update: Update, context: CallbackContext):
        state = "MENU_DISPLAYED"
        chat_id = update.effective_chat.id

        context.bot.send_message(chat_id,
                                 f'<b>{text["main_page"]}</b>',
                                 reply_markup=ReplyKeyboardMarkup(
                                     self.menu_buttons, resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened main menu. Returned state: {state}")
        return state

    def categories(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "CATEGORIES"
        buttons = parser(API_URL=API_URL + "categories/",
                         API_auth=api_auth,
                         key='name')

        context.bot.send_message(chat_id,
                                 f'<b>{text["category"]}</b>',
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=2,
                                         footer_buttons=[
                                             KeyboardButton(
                                                 button["back"])]
                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened categories. Returned state: {state}")
        return state

    def products(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "PRODUCTS"
        raw_buttons = parser(API_URL=API_URL + "products/",
                             API_auth=api_auth,
                             key='name')
        print(requests.get(url=API_URL + "products/", auth=api_auth).json())
        buttons = raw_buttons

        context.bot.send_message(chat_id,
                                 f'<b>{text["product"]}</b>',
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=1,
                                         footer_buttons=[
                                             KeyboardButton(
                                                 button["back"])]

                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened products. Returned state: {state}")
        return state

    def product_details(self, update: Update, context):
        update.effective_message.reply_text("Yes, you chose something")
