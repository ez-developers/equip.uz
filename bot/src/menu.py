from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext
from bot.utils.build_menu import build_menu
from bot.utils._reqs import parser, target_category_id, products_list, product_details
from backend.settings import API_URL, API_AUTHENTICATION
import logging
import json

j = json.load(open("bot/assets/text.json", "r"))
text = j["texts"]
button = j["buttons"]["menu"]


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
                                 f'{text["main_page"]}',
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
                         API_auth=API_AUTHENTICATION,
                         key='name')

        context.bot.send_message(chat_id,
                                 f'{text["category"]}',
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
        target_id = target_category_id(update.message.text)
        state = "PRODUCTS"
        buttons = products_list(target_id)

        context.bot.send_message(chat_id,
                                 f'{text["product"]}',
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

    def product_details(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        requested_product = update.message.text
        product = product_details(requested_product)
        context.bot.send_message(chat_id,
                                 f"""<b>{product['name']}</b>
                                 
<b>Описание:</b>
{product['description']}
                                 
<b>Цена:</b>
{product["price"]}""", parse_mode='HTML')
