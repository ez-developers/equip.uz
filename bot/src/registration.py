from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      error)
from telegram.ext import CallbackContext
from telegram.keyboardbutton import KeyboardButton
from backend.settings import API_URL, API_AUTHENTICATION
from bot.src.menu import Menu
from bot.src.conversation import Conversation
from bot.utils._reqs import get
from bot.utils.json_to_dict import json_to_dict
from bot.utils.sms_api import send_sms, sms_text
import logging
import requests
import random

txt = json_to_dict('bot/assets/text.json')


class Registration:
    """ 
    Base class for registration
    """

    def is_private_chat(self, chat_id: int):
        if chat_id > 0:
            return True
        else:
            return False

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user = update.effective_user
        if self.is_private_chat(chat_id):
            all_users = []
            user_objects = get('users')
            for i in user_objects:
                all_users.append(i["user_id"])
            if chat_id in all_users:
                return self.check_data(update, context, chat_id)
            else:
                # Sending user info to backend server
                payload = {
                    "user_id": chat_id,
                    "name": user.full_name,
                    "username": "@" + user.username if user.username else None,
                }
                requests.post(API_URL + 'adduser/',
                              auth=API_AUTHENTICATION,
                              json=payload)
                context.bot.send_message(chat_id,
                                         txt["texts"]["greeting"],
                                         parse_mode='HTML')
                return self.request_name(update, context)
        else:
            return  # The bot is working in the group.

    def check_data(self, update, context, chat_id):
        user = get(f'users/{chat_id}')
        if user['phone_number'] is None:
            return self.request_name(update, context)
        else:
            return Menu().display(update, context)

    def request_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "NAME"
        context.bot.send_message(chat_id,
                                 txt["texts"]["request_name"],
                                 reply_markup=ReplyKeyboardRemove())
        logging.info(
            f"User {chat_id} has been greeted and  requested name. Returning state {state}")
        return state

    def get_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        name_input = update.effective_message.text
        try:
            if int(name_input):
                update.effective_message.reply_text(
                    "Исм сонлардан иборат бўлиши мумкин эмас!")
        except ValueError:
            if name_input[0].isupper():
                payload = {
                    "user_id": chat_id,
                    "name": name_input
                }
                req = requests.put(API_URL + f"users/{chat_id}",
                                   auth=API_AUTHENTICATION,
                                   json=payload)
                if req.status_code == 400 and req.reason == "Bad Request":
                    update.effective_message.reply_text(
                        "Исм 30 ҳарф ёки ундан кам бўлганлигига ишонч ҳосил қилинг."
                    )
                if req.status_code == 200:
                    update.effective_message.reply_text(
                        f"Танишганимдан хурсандман, {update.effective_message.text}!")
                    return self.request_phone(update, context)
            else:
                update.effective_message.reply_text(
                    "Исмни катта ҳарф билан ёзинг")

    def request_phone(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "REQUESTING_PHONE"
        context.bot.send_message(chat_id=chat_id,
                                 text=txt['texts']['request_phone'],
                                 reply_markup=ReplyKeyboardMarkup([
                                     [KeyboardButton(
                                         txt['buttons']['send_phone'], request_contact=True)],
                                 ], resize_keyboard=True),
                                 parse_mode='HTML')
        logging.info(
            f"{chat_id} is being requested his phone number. Returning state: {state}")
        return state

    def send_code(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "CODE_CHECK"
        code = random.randint(100000, 1000000)
        payload = {
            'sms_code': code
        }
        context.user_data.update(payload)
        phone = context.user_data['phone_number']

        send_sms(phone, sms_text(code))
        update.effective_message.reply_text(
            "Код юборилди. Фаоллаштириш учун уни киритинг.",
            reply_markup=ReplyKeyboardMarkup([
                [KeyboardButton(txt['buttons']['resend_code'])],
                [KeyboardButton(txt['buttons']['reenter_phone'])]
            ], resize_keyboard=True))

        return state

    def get_phone(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        message = update.effective_message

        if message.contact:
            phone = message.contact.phone_number
            if phone[1:4] == '998':
                phone = phone[1:4]

            if phone[:3] == '998':
                context.user_data.update({
                    "phone_number": phone
                })
                user = get(f'users/{chat_id}')
                user['phone_number'] = context.user_data['phone_number'][3:]

                requests.put(API_URL + f'users/{chat_id}',
                             auth=API_AUTHENTICATION,
                             json=user)
                return Conversation().display(update, context,
                                              after_registration=True)
            else:
                update.effective_message.reply_text(
                    "Ҳозирча биз фақат Ўзбекистондаги рақамларни қабул қиламиз!")

        else:
            phone = update.message.text[1:]
            if phone[:3] == '998' and len(phone) == 12 and int(phone):
                context.user_data.update({
                    "phone_number": phone
                })

                user = get(f'users/{chat_id}')
                user['phone_number'] = context.user_data['phone_number'][3:]

                requests.put(API_URL + f'users/{chat_id}',
                             auth=API_AUTHENTICATION,
                             json=user)
                return Conversation().display(update, context,
                                              after_registration=True)
            else:
                self.request_phone(update, context)

    def confirming_phone(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        user_input = update.message.text

        try:
            if int(user_input) == context.user_data['sms_code']:
                user = get(f'users/{chat_id}')
                user['phone_number'] = context.user_data['phone_number'][3:]

                requests.put(API_URL + f'users/{chat_id}',
                             auth=API_AUTHENTICATION,
                             json=user)

                update.effective_message.reply_text(
                    'Ажойиб, рақамингиз тасдиқланди!')
                return Conversation().display(update, context, after_registration=True)
            else:
                update.effective_message.reply_text(
                    "Код нотўғри. Яна бир бор уриниб кўринг!")
        except ValueError:
            update.effective_message.reply_text('Код фақат рақамлардан иборат')
