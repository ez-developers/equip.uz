from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.error import BadRequest, Unauthorized
from bot.utils._reqs import get
from bot.utils.admin import is_admin
from bot.src.menu import Menu
import json
import logging
import time

j = json.load(open("bot/assets/text.json", "r"))
text = j['texts']
button = j['buttons']


class Broadcast:

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "BROADCAST"
        if is_admin(chat_id):
            context.bot.send_message(chat_id,
                                     text['send_broadcast_media'],
                                     reply_markup=ReplyKeyboardMarkup(
                                         [
                                             [KeyboardButton(button['cancel'])]
                                         ], resize_keyboard=True
                                     ),
                                     parse_mode='HTML')
            logging.info(
                f"Admin {chat_id} has started new broadcast. Returned state: {state}")
            return state
        else:
            return Menu().display(update, context)

    def all(self, update: Update, context: CallbackContext):
        message = update.effective_message
        users = get('users')
        chat_ids = []
        sent_to = []
        for i in users:
            if i['notifications'] is True:
                chat_ids.append(i['user_id'])

        update.effective_message.reply_text(
            "Мен ҳаммага юборишни бошладим", reply_markup=ReplyKeyboardRemove())
        for user in chat_ids:
            try:
                msg = message.copy(user)
                sent_to.append(msg)
                time.sleep(0.05)
            except Unauthorized:
                continue
        update.effective_message.reply_text(
            f"Ахборотларни юбориш тугади! Етказиб берилди {len(sent_to)}/{len(chat_ids)}")
        return Menu().display(update, context)
