from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          Defaults,
                          CallbackContext)
from telegram import Update
from dotenv import load_dotenv
from bot.src.commands import Command
from bot.src.language import get_language
from bot.utils.states import *
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


copy = Command()


def main():
    load_dotenv()
    defaults = Defaults(parse_mode="HTML", disable_notification=True)
    updater = Updater(token=os.getenv('API_TOKEN'), defaults=defaults)
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', callback=Command().start)
        ],
        states={
            LANGUAGE: [
                MessageHandler(Filters.text, get_language)
            ]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
