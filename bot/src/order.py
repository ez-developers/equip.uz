import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
# from bot.utils.build_menu import build_menu


class Order:

    def __init__(self):
        pass

    def category_menu(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id

        # context.bot.send_message(chat_id, "<b>Main menu</b>",
        #                          reply_markup=ReplyKeyboardMarkup(
        #                              (), resize_keyboard=True),
        #                          parse_mode='HTML')


headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic YWRtaW46TnVyaWRkaW5Jc2xhbW92MTIzNA=="
}
x = requests.get("http://localhost:8000/api/products/", headers=headers)
print(x.json())

body = {
    "name": "Торвотру",
    "description": "Очень классная девушка",
    "price": "1.12",
    "category": 1
}

y = requests.post("http://localhost:8000/api/products/",
                  headers=headers, json=body)
print(y.json())
print(y.status_code)
