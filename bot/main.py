from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          MessageHandler,
                          Filters)
from dotenv import load_dotenv
from callbacks.start import start
import os


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ],
        states={},
        fallbacks=[]
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()
