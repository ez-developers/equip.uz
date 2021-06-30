from telegram.ext import CallbackContext
from .language import ask_language
from bot.utils.states import LANGUAGE
from telegram import Update


class Command:

    def __init__(self):
        self.state = 1

    def start(self, update, context):
        print(self)
        print(update, "start")

    def help_command(self, update, context):
        print(self, 'help', update.effective_chat.id)

    def menu(self):
        print(self, 'menu')

    def reset(self):
        print(self, 'reset')

