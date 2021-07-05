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
from bot.utils.filter import filterCategories, filterProducts
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

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
            "MENU_DISPLAYED": [
                MessageHandler(Filters.regex(
                    "See the catalog"), menu.categories)
            ],
            "CATEGORIES": [
                MessageHandler(Filters.regex('Back'), menu.display),
                MessageHandler(filterCategories, menu.products)
            ],
            "PRODUCTS": [
                MessageHandler(Filters.regex('Back'), menu.categories),
                MessageHandler(filterProducts, menu.product_details)
            ]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
