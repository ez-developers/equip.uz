from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup
import json
import logging

j = json.load(open("bot/assets/text.json", "r"))
text = j["texts"]
button = j["buttons"]


class Conversation:
    def display(self,
                update: Update,
                context: CallbackContext,
                after_registration: bool = False):
        chat_id = update.effective_chat.id
        state = "CONVERSATION"

        if after_registration:

            context.bot.send_message(chat_id,
                                     text['choose_type_conversation'],
                                     reply_markup=ReplyKeyboardMarkup([
                                         [button["skip"]],
                                         [button["type_text"],
                                          button["type_photo"]],
                                         [button["type_video"],
                                             button["type_audio"]]
                                     ], resize_keyboard=True),
                                     parse_mode='HTML')

        else:
            context.bot.send_message(chat_id,
                                     text['choose_type_conversation'],
                                     reply_markup=ReplyKeyboardMarkup([
                                         [button["type_text"],
                                          button["type_photo"]],
                                         [button["type_video"],
                                          button["type_audio"]],
                                         [button["menu"]["back"]]
                                     ], resize_keyboard=True),
                                     parse_mode='HTML')
        logging.info(
            f"User {chat_id} is choosing the type of conversation. Returned state: {state}")
        return state

    def accept_request(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        text = update.effective_message.text
        if text == "Текстовое сообщение":
            update.effective_message.reply_text("You chose TEXT type")
        elif text == "Фото":
            update.effective_message.reply_text("You chose PHOTO type")
        elif text == "Видео":
            update.effective_message.reply_text("You chose VIDEO type")
        elif text == "Аудио-голос":
            update.effective_message.reply_text("You chose AUDIO type")
