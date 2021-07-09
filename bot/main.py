from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          CallbackContext,)
from dotenv import load_dotenv
from bot.src.menu import Menu
from bot.src.registration import Registration
from bot.src.commands import Command
from bot.utils.filter import filterCategories, filterProducts
import os
import logging
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

menu = Menu()
registration = Registration()
commands = Command()
j = json.load(open("bot/assets/text.json", "r"))
menu_buttons = j['buttons']['menu']


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', menu.display)
        ],
        states={
            "MENU_DISPLAYED": [
                MessageHandler(Filters.regex(
                    menu_buttons["order"]), menu.categories)
            ],
            "CATEGORIES": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.display),
                MessageHandler(filterCategories, menu.products)
            ],
            "PRODUCTS": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.categories),
                MessageHandler(filterProducts, menu.product_details)
            ]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
