from .language import ask_language
from bot.utils.states import LANGUAGE
from telegram import Update
from telegram.ext import CallbackContext

temp_database = []


def start(update: Update, context: CallbackContext) -> LANGUAGE:
    if len(temp_database) != 0:
        for i in temp_database:
            a = i.get("id")
            print(a)

    ask_language(update, context)
    return LANGUAGE


def help_command():
    print('help')


def menu():
    print('menu')


def reset():
    print('reset')
