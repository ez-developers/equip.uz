from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import logging
from typing import Dict, List
from telegram.keyboardbutton import KeyboardButton

from telegram.replykeyboardmarkup import ReplyKeyboardMarkup


class Registration:
    """ 
    Base class for registration
    """

    def __init__(self,
                 languages_buttons: List[List[InlineKeyboardButton]
                                         ] or List[List[KeyboardButton]]
                 = [
                     [InlineKeyboardButton(
                         "🇺🇿 Ўзбек тили", callback_data='uz')],
                     [InlineKeyboardButton("🇷🇺 Русский язык", callback_data='ru'),
                      InlineKeyboardButton("🇺🇸 English", callback_data='en')]
                 ],
                 language_text: str = "Тилни танланг\nВыберите язык\nChoose the language",
                 states: Dict = {},
                 inline=True
                 ):
        """__init__ Initialize Registration configs

        Args:
            languages (List[List[InlineKeyboardButton]], optional): This will parse the texts and return a list of buttons in your request. Defaults to [ [InlineKeyboardButton('Uzbek', callback_data='uz'), InlineKeyboardButton("English", callback_data='en')], [InlineKeyboardButton("Russian", callback_data='ru')] ].
            language_text (str, optional): This is text message that is sent out to the user with buttons attached. Defaults to "language".
        """
        self.languages = languages_buttons
        self.language_text = language_text
        self.states = states
        self.inline = inline

    def request_language(self, update: Update, context: CallbackContext):
        """request_language sends a message to the user with buttons attached.

        Args:
            inline (bool, optional): Choose whether buttons are inline or not. Defaults to True.

        Note: Passing list of 'KeyboardButton' type buttons requires `inline=False`
        """
        chat_id = update.effective_chat.id
        logging.info(f"User {chat_id} is choosing a language")
        if self.inline:
            context.bot.send_message(chat_id,
                                     self.language_text,
                                     reply_markup=InlineKeyboardMarkup(self.languages))
        else:
            context.bot.send_message(chat_id,
                                     self.language_text,
                                     reply_markup=ReplyKeyboardMarkup(self.languages, resize_keyboard=True))
        return self.states["LANGUAGE"]

    def get_language(self, update: Update, context: CallbackContext):
        if update.message:
            pass
        elif update.callback_query:
            pass
        else:
            pass

    def do_something(self, update: Update, context: CallbackContext):
        print("FINALLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
