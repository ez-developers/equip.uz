from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          Defaults,
                          CallbackContext)
from telegram import Update, KeyboardButton
from dotenv import load_dotenv
from bot.src.registration import Registration
from bot.src.language import get_language
from bot.utils.states import *
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

states = {
    "LANGUAGE": 1,
    "NAME": 2,
    "PHONE": 3,
    "PHONE_CODE": 4,
}

registration = Registration(states=states)


def main():
    load_dotenv()
    defaults = Defaults(parse_mode="HTML", disable_notification=True)
    updater = Updater(token=os.getenv('API_TOKEN'), defaults=defaults)
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler(
                'start', callback=registration.request_language)
        ],
        states={
            1: [
                MessageHandler(Filters.text, registration.do_something),
            ]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
