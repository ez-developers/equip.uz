from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup
from backend.settings import GROUP_ID
from bot.utils._reqs import get
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

    def route_request(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user_input = update.effective_message.text
        if user_input == button["type_text"]:
            update.effective_message.reply_text(text["text_type"],
                                                reply_markup=ReplyKeyboardMarkup([
                                                    [button["menu"]["back"]]
                                                ], resize_keyboard=True),
                                                parse_mode='HTML')
            return "TEXT_TYPE"
        elif user_input == button["type_photo"]:
            update.effective_message.reply_text(text["photo_type"],
                                                reply_markup=ReplyKeyboardMarkup([
                                                    [button["menu"]["back"]]
                                                ], resize_keyboard=True),
                                                parse_mode='HTML')
            return "PHOTO_TYPE"
        elif user_input == button["type_video"]:
            update.effective_message.reply_text(text["video_type"],
                                                reply_markup=ReplyKeyboardMarkup([
                                                    [button["menu"]["back"]]
                                                ], resize_keyboard=True),
                                                parse_mode='HTML')
            return "VIDEO_TYPE"
        elif user_input == button["type_audio"]:
            update.effective_message.reply_text(text["audio_type"],
                                                reply_markup=ReplyKeyboardMarkup([
                                                    [button["menu"]["back"]]
                                                ], resize_keyboard=True),
                                                parse_mode='HTML')
            return "AUDIO_TYPE"

    def accept_request(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user_request = update.effective_message
        user = get(f"users/{chat_id}")
        context.bot.forward_message(GROUP_ID,
                                    from_chat_id=chat_id,
                                    message_id=user_request.message_id)
