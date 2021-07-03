from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext
from bot.utils.build_menu import build_menu


class Menu:
    def __init__(self):
        pass

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        menu_markup = [
            [KeyboardButton("Start shopping")],
            [KeyboardButton("Contact us"), KeyboardButton("Sales")],
            [KeyboardButton("Settings")]
        ]
        context.bot.send_message(chat_id, "<b>Main menu</b>",
                                 reply_markup=ReplyKeyboardMarkup(
                                     menu_markup, resize_keyboard=True),
                                 parse_mode='HTML')
