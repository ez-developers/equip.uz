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
from bot.src.conversation import Conversation
from bot.utils.filter import filterCategories, filterProducts
import os
import logging
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

menu = Menu()
registration = Registration()
conversation = Conversation()
j = json.load(open("bot/assets/text.json", "r"))
menu_buttons = j['buttons']['menu']
buttons = j['buttons']


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', registration.start)
        ],
        states={
            "NAME": [
                MessageHandler(Filters.text, registration.get_name)
            ],
            "REQUESTING_PHONE": [
                MessageHandler(Filters.text | Filters.contact,
                               registration.get_phone)
            ],
            "CODE_CHECK": [
                MessageHandler(Filters.regex(
                    buttons['reenter_phone']), registration.request_phone),
                MessageHandler(Filters.regex(
                    buttons['resend_code']), registration.send_code),
                MessageHandler(Filters.text, registration.confirming_phone)
            ],
            "MENU_DISPLAYED": [
                MessageHandler(Filters.regex(
                    menu_buttons["order"]), menu.categories),
                MessageHandler(Filters.regex(
                    menu_buttons["contact"]), Conversation().display),
                MessageHandler(Filters.regex(
                    menu_buttons["settings"]), menu.settings)
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
            ],
            "SETTINGS": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.display),
                MessageHandler(Filters.regex(buttons["notification_on"]) |
                               Filters.regex(buttons["notification_off"]),
                               menu.change_notification_status),
                MessageHandler(Filters.regex(
                    buttons["change_phone"]), registration.request_phone),
                MessageHandler(Filters.regex(
                    buttons["change_name"]), menu.change_name),
            ],
            "EDITING_NAME": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.settings),
                MessageHandler(Filters.text, menu.get_name),
            ],
            "CONVERSATION": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.display),
                MessageHandler(Filters.regex(buttons['skip']), menu.display),
                MessageHandler(Filters.regex(buttons['type_text']) |
                               Filters.regex(buttons['type_photo']) |
                               Filters.regex(buttons['type_video']) |
                               Filters.regex(buttons['type_audio']),
                               Conversation().accept_request),
            ]
        },
        fallbacks=[
            CommandHandler('start', registration.start)
        ]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
