from telegram.ext import CallbackContext
from telegram import Update


class Command:

    def __init__(self):
        self.state = None

    def start(self, update, context):
        pass

    def help_command(self, update, context):
        print(self, 'help', update.effective_chat.id)

    def menu(self):
        print(self, 'menu')

    def reset(self):
        print(self, 'reset')
