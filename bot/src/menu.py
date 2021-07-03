from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext
from bot.utils.build_menu import build_menu
from bot.src.order import Order
from bot.utils._reqs import parser
from backend.settings import API_URL
from requests.auth import HTTPBasicAuth
import logging


class Menu:
    def __init__(self):
        self.menu_buttons = [
            [KeyboardButton("Start shopping")],
            [KeyboardButton("Contact us"), KeyboardButton("Sales")],
            [KeyboardButton("Settings")]
        ]

    def display(self, update: Update, context: CallbackContext):
        state = "MENU_DISPLAYED"
        chat_id = update.effective_chat.id

        context.bot.send_message(chat_id, "<b>Main menu</b>",
                                 reply_markup=ReplyKeyboardMarkup(
                                     self.menu_buttons, resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened main menu. Returned state: {state}")
        return state

    def categories(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        buttons = parser(API_URL=API_URL + "categories/",
                         API_auth=HTTPBasicAuth('admin', 'admin'),
                         key='name')

        context.bot.send_message(chat_id, "<b>Choose a category</b>",
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=2,
                                         footer_buttons=[
                                             KeyboardButton("Back")]

                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        return "CATEGORIES"

    def products(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id

        buttons = parser(API_URL=API_URL + "products/",
                         API_auth=HTTPBasicAuth('admin', 'admin'),
                         key='name')

        context.bot.send_message(chat_id, "<b>Choose a product</b>",
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=2,
                                         footer_buttons=[
                                             KeyboardButton("Back")]

                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        return "PRODUCTS"

    def product_details(self, update: Update, context):
        update.effective_message.reply_text("Yes, you chose something")
