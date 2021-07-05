from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.keyboardbutton import KeyboardButton
from bot.utils.build_menu import build_menu
from requests.auth import HTTPBasicAuth
from bot.utils._reqs import parser
from backend.settings import API_URL


class Order:

    def __init__(self):
        pass

    @staticmethod
    def categories(update: Update, context: CallbackContext):
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

                                     )
                                 ),
                                 parse_mode='HTML')
