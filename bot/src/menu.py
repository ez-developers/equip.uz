from telegram import ReplyKeyboardMarkup, Update, KeyboardButton, ChatAction
from telegram.ext import CallbackContext
from bot.utils.build_menu import build_menu
from bot.utils._reqs import (parser,
                             target_category_id,
                             products_list,
                             product_details,
                             notification_on,
                             get)
from bot.utils.get_photo_id import get_photo_id
from backend.settings import API_URL, API_AUTHENTICATION, BASE_DIR
import logging
import time
import json
import requests

j = json.load(open("bot/assets/text.json", "r"))
text = j["texts"]
button = j["buttons"]
menu_button = j["buttons"]["menu"]


class Menu:
    def __init__(self):
        self.menu_buttons = [
            [KeyboardButton(menu_button["order"])],
            [KeyboardButton(menu_button["contact"]),
             KeyboardButton(menu_button["promo"])],
            [KeyboardButton(menu_button["settings"])]
        ]

    def display(self, update: Update, context: CallbackContext):
        state = "MENU_DISPLAYED"
        chat_id = update.effective_chat.id

        context.bot.send_message(chat_id,
                                 f'{text["main_page"]}',
                                 reply_markup=ReplyKeyboardMarkup(
                                     self.menu_buttons, resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened main menu. Returned state: {state}")
        return state

    def categories(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "CATEGORIES"
        buttons = parser(API_URL=API_URL + "categories/",
                         API_auth=API_AUTHENTICATION,
                         key='name')

        context.bot.send_message(chat_id,
                                 f'{text["category"]}',
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=2,
                                         footer_buttons=[
                                             KeyboardButton(
                                                 menu_button["back"])]
                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened categories. Returned state: {state}")
        return state

    def products(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        target_id = target_category_id(update.message.text)
        state = "PRODUCTS"
        buttons = products_list(target_id)

        context.bot.send_message(chat_id,
                                 f'{text["product"]}',
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[KeyboardButton(
                                             s) for s in buttons],
                                         n_cols=1,
                                         footer_buttons=[
                                             KeyboardButton(
                                                 menu_button["back"])]

                                     ), resize_keyboard=True
                                 ),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened products. Returned state: {state}")
        return state

    def product_details(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        requested_product = update.message.text
        product = product_details(requested_product)
        a = str(product['price'])
        formatted_price = ' '.join([a[::-1][i:i+3]
                                    for i in range(0, len(a), 3)])[::-1]

        try:
            file_id = context.bot_data['product_' + str(product['id'])]
            context.bot.send_photo(chat_id,
                                   photo=file_id,
                                   caption=f"""<b>{product['name']}</b>
                                 
<b>Описание:</b>
{product['description']}
                                 
<b>Цена:</b>
{formatted_price} сум""", parse_mode='HTML')
            return
        except KeyError:
            pass
        if product['image'][-1] == '/':
            product['image'] = product['image'][:-1]
        context.bot.send_chat_action(chat_id,
                                     action=ChatAction.UPLOAD_PHOTO)
        # time.sleep(0.5)
        msg = context.bot.send_photo(chat_id,
                                     photo=open(str(BASE_DIR) +
                                                product['image'], 'rb'),
                                     caption=f"""<b>{product['name']}</b>
                                 
<b>Описание:</b>
{product['description']}
                                 
<b>Цена:</b>
{formatted_price} сум""", parse_mode='HTML')
        payload = {
            'product_' + str(product['id']): get_photo_id(msg.photo)
        }
        print(payload)
        context.bot_data.update(payload)

    def settings(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "SETTINGS"
        notif_status = notification_on(chat_id)
        notifcation_button = button["notification_off"] if notif_status else button["notification_on"]

        buttons = [
            [button["change_phone"],
             button["change_name"]],
            [notifcation_button],
            [menu_button['back']]
        ]
        context.bot.send_message(chat_id,
                                 text["settings"],
                                 reply_markup=ReplyKeyboardMarkup(
                                     buttons, resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} opened settings. Returned state: {state}")
        return state

    def change_notification_status(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user = get(f'users/{chat_id}')
        if notification_on(chat_id):
            user['notifications'] = False
            update.effective_message.reply_text(
                "Вы отписались от уведомлений!")
        else:
            user['notifications'] = True
            update.effective_message.reply_text(
                "Подписка на уведомления возобновлена!")
        requests.put(API_URL + f'users/{chat_id}',
                     auth=API_AUTHENTICATION,
                     json=user,
                     headers={'Content-Type': 'application/json'})
        logging.info(
            f"User {chat_id} has changed his notification preferences to {user['notifications']}")
        return self.settings(update, context)

    def change_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "EDITING_NAME"
        context.bot.send_message(chat_id,
                                 text["enter_name"],
                                 reply_markup=ReplyKeyboardMarkup([
                                     [menu_button["back"]]
                                 ], resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"User {chat_id} is changing name. Returned state: {state}")
        return state

    def get_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        name = update.effective_message.text

        user = get(f'users/{chat_id}')
        user['name'] = name
        requests.put(API_URL + f"users/{chat_id}",
                     auth=API_AUTHENTICATION,
                     json=user)
        update.effective_message.reply_text(
            "<b>Готово! ✅</b>", parse_mode='HTML')
        return self.settings(update, context)
