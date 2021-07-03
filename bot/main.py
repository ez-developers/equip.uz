from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          Defaults,
                          CallbackContext,)
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv
from bot.utils.json_to_dict import json_to_dict
from bot.src.menu import Menu
from bot.utils.build_menu import build_menu
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

t = json_to_dict('bot/assets/text.json')

temp_database = {}


def lang(update):
    chat_id = update.effective_chat.id
    return temp_database[chat_id]['lang']


def send_message(update, context, message_key: str = "no valid text"):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text=t[lang(update)][message_key])


def start(update: Update, context: CallbackContext):
    user = update.message.chat
    full_name = update.message.from_user.full_name
    if user.id < 0:
        pass
    elif user.id > 0:
        if "user is not in the database":
            # TODO: Backend API call
            temp_database.update({
                user.id: {
                    "full_name": full_name
                }
            })
            request_language(update, context)
            return "LANGUAGE"
        else:
            # TODO: Backend API call
            if "user's data is missing":
                # TODO: Backend API call
                print("Delete from the database")
                start(update, context)
                return "LANGUAGE"
            elif "user's data is complete":
                print("Get him to the main menu")
                return "MAIN_MENU"


def request_language(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    try:
        query = update.callback_query
        query.answer()
        # TODO: Backend API call
        temp_database.update({
            chat_id: {
                "lang": query.data
            }
        })
        query.delete_message()
        context.bot.send_message(chat_id=chat_id,
                                 text=t[chat_id]['lang'],
                                 parse_mode='HTML')
        request_name(update, context)
        return "NAME"
    except AttributeError:
        pass


def request_name(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text=t[lang(update)]['name'])


def accept_name(update, context):
    message = update.effective_message
    if len(message.text.split()) == 1:
        send_message(update, context, "name_accepted")
        request_phone(update, context)
        # TODO: Backend API call
        return "PHONE"
    else:
        send_message(update, context, message_key="name_error")


def request_phone(update: Update, context: CallbackContext):
    button = [
        [KeyboardButton(t[lang(update)]["phone_button"], request_contact=True)]
    ]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=t[lang(update)]["phone"],
                             reply_markup=ReplyKeyboardMarkup(button,
                                                              resize_keyboard=True),
                             parse_mode='HTML')
    return "PHONE"


def accept_phone(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.contact or message.reply_to_message:
        if (message.contact.phone_number[:3] == '998' or
                message.contact.phone_number[1:4] == '998'):
            # TODO: Backend API call
            return "MAIN_MENU"
        else:
            request_phone(update, context)
    elif message.text:
        phone = message.text[1:]
        if phone[:3] == '998' and len(phone) == 12 and int(phone[1:]):
            # TODO: Backend API call
            return "MAIN_MENU"
        else:
            request_phone(update, context)
    else:
        request_phone(update, context)


def consulting(update: Update, context: CallbackContext):
    pass


def main_menu(update: Update, context: CallbackContext):
    menu = build_menu(
        [
            ["Order"],
            ["Contact", "Akcii"],
            ["Settings"]
        ]
    )

    update.effective_message.reply_text("Main menu",
                                        reply_markup=ReplyKeyboardMarkup())
    return "MAIN_MENU"


menu = Menu()


def main():
    load_dotenv()
    # defaults = Defaults(parse_mode="HTML", disable_notification=True)
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', menu.display)
        ],
        states={
            "LANGUAGE": [
                CallbackQueryHandler(request_language)
            ],
            "NAME": [
                MessageHandler(Filters.text, accept_name)
            ],
            "PHONE": [

            ],
            "MAIN_MENU": [

            ],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
