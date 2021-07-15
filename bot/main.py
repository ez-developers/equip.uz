from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters,
                          CallbackQueryHandler,
                          CallbackContext,)
from dotenv import load_dotenv
from ptbcontrib.reply_to_message_filter import ReplyToMessageFilter
from backend.settings import BOT_ID
from bot.src.menu import Menu
from bot.src.registration import Registration
from bot.src.conversation import Conversation
from bot.src.promo import Promo
from bot.src.group import Group
from bot.utils.filter import FilterButton
import os
import logging
import json

load_dotenv()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG if os.getenv('DEBUG') == "True"
                    else logging.INFO)

menu = Menu()
registration = Registration()
conversation = Conversation()
promo = Promo()
group = Group()
j = json.load(open("bot/assets/text.json", "r"))
menu_buttons = j['buttons']['menu']
buttons = j['buttons']


def main():
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    main_conversation = ConversationHandler(
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
                    menu_buttons["contact"]), conversation.display),
                MessageHandler(Filters.regex(
                    menu_buttons["settings"]), menu.settings),
                MessageHandler(Filters.regex(
                    menu_buttons["promo"]), promo.display)
            ],
            "CATEGORIES": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.display),
                MessageHandler(FilterButton("categories"), menu.products)
            ],
            "PRODUCTS": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), menu.categories),
                MessageHandler(FilterButton("products"), menu.product_details)
            ],
            "PROMO_DISPLAYED": [
                CallbackQueryHandler(promo.back_to_menu, pattern="exit"),
                CallbackQueryHandler(promo.back_to_menu, pattern="like"),
                CallbackQueryHandler(promo.back_to_menu, pattern="prev"),
                CallbackQueryHandler(promo.back_to_menu, pattern="next")
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
                               conversation.route_request),
            ],
            "TEXT_TYPE": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), conversation.display),
                MessageHandler(Filters.text, conversation.accept_request)
            ],
            "PHOTO_TYPE": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), conversation.display),
                MessageHandler(Filters.photo, conversation.accept_request)
            ],
            "VIDEO_TYPE": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), conversation.display),
                MessageHandler(Filters.video, conversation.accept_request)
            ],
            "AUDIO_TYPE": [
                MessageHandler(Filters.regex(
                    menu_buttons["back"]), conversation.display),
                MessageHandler(Filters.audio |
                               Filters.voice,
                               conversation.accept_request)
            ]
        },
        fallbacks=[
            CommandHandler('start', registration.start)
        ]
    )

    dispatcher.add_handler(main_conversation)
    dispatcher.add_handler(MessageHandler(
        ReplyToMessageFilter(Filters.user(BOT_ID)), group.reply_to_user))

    updater.start_polling()
    updater.idle()
