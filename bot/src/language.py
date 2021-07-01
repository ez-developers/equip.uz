import json
import os
from telegram import ReplyKeyboardMarkup, Update, Message
from telegram.ext import CallbackContext

txt = json.load(open("bot/assets/texts.json", 'r'))


def ask_language(update: Update, context: CallbackContext) -> Message:
    chat = update.effective_chat.id
    return context.bot.sendMessage(chat_id=chat,
                                   text='Choose a language please',
                                   reply_markup=ReplyKeyboardMarkup(
                                       [
                                           ['English'], ['Russian'], ['Uzbek']
                                       ], resize_keyboard=True
                                   ))


def get_language(update, context):
    print(update.message)
