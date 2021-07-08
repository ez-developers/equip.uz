from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup,
                      error
                      )
from telegram.ext import CallbackContext
import logging
import json
from typing import Dict, List
from telegram.keyboardbutton import KeyboardButton
from bot.src.error import ButtonError
from bot.utils.json_to_dict import json_to_dict

txt = json_to_dict('bot/assets/text.json')


class Registration:
    """ 
    Base class for registration
    """

    def __init__(self,
                 language_buttons: List[List[InlineKeyboardButton]
                                        ] or List[List[KeyboardButton]]
                 = [
                     [InlineKeyboardButton(
                         "🇺🇿 Ўзбек тили", callback_data='uz')],
                     [InlineKeyboardButton("🇷🇺 Русский язык", callback_data='ru'),
                      InlineKeyboardButton("🇺🇸 English", callback_data='en')]
                 ],
                 inline=True,
                 language: str = None,
                 phone_text="Please provide your phone number",
                 phone_button: List[InlineKeyboardButton] = [
                     [KeyboardButton(
                         "Send my phone",
                         request_contact=True)]
                 ],

                 ):
        """__init__ Initialize Registration configs

        Args:
            languages (List[List[InlineKeyboardButton]], optional): This will parse the texts and return a list of buttons in your request. Defaults to [ [InlineKeyboardButton('Uzbek', callback_data='uz'), InlineKeyboardButton("English", callback_data='en')], [InlineKeyboardButton("Russian", callback_data='ru')] ].
            language_text (str, optional): This is text message that is sent out to the user with buttons attached. Defaults to "language".
        """
        self.languages = language_buttons
        self.inline = inline
        self.phone_text = phone_text
        self.phone_button = phone_button
        self.language = language

    def request_language(self, update: Update, context: CallbackContext):
        """request_language sends a message to the user with buttons attached.

        Args:
            inline (bool, optional): Choose whether buttons are inline or not. Defaults to True.

        Note: Passing list of 'KeyboardButton' type buttons requires `inline=False`
        """
        state = "LANGUAGE"
        chat_id = update.effective_chat.id
        logging.info(
            f"User {chat_id} is choosing a language. Returning state: {state}")
        try:
            if self.inline:
                context.bot.send_message(chat_id,
                                         "Choose a language Please",
                                         reply_markup=InlineKeyboardMarkup(self.languages))
            else:
                context.bot.send_message(chat_id,
                                         "Choose a language Please",
                                         reply_markup=ReplyKeyboardMarkup(self.languages, resize_keyboard=True))
        except error.BadRequest:
            raise ButtonError(
                "Please set 'inline=False' if you are using KeyboardButton")
        return state

    def get_language(self, update: Update, context: CallbackContext):
        """get_language handles user input for chosen language

        Returns:
            str: Returns callback_data if the buttons were type of InlineKeyboardButton, else returns string of chosen button type of KeyboardButton
        """
        if update.message:
            return update.message.text
        elif update.callback_query:
            query = update.callback_query
            query.answer()
            query.delete_message()
            return query.data

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
