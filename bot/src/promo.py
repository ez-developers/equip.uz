from telegram import Update, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
from telegram.ext import CallbackContext
from bot.src.menu import Menu
from bot.utils.get_photo_id import get_photo_id
from bot.utils._reqs import get
from backend.settings import API_URL, API_AUTHENTICATION, BASE_DIR
import json
import requests
import logging

j = json.load(open("bot/assets/text.json", "r"))
text = j["texts"]
button = j["buttons"]


class Promo:

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "PROMO_DISPLAYED"
        promo_ids = []

        promos = requests.get(
            API_URL + "promo", auth=API_AUTHENTICATION).json()

        if len(promos) == 0:
            update.effective_message.reply_text(
                "<b>Действующих акций пока нет 😔</b>", parse_mode='HTML')
            return
        for promo in promos:
            promo_ids.append(promo['id'])
        context.user_data.update(
            {
                "current_index": 0,
                "promo_ids": promo_ids,
                "first_promo": promo_ids[0],
                "last_promo": promo_ids[-1]
            }
        )
        i = context.user_data['current_index']
        promo_text = f"<b>{promos[i]['name']}</b>\n\n{promos[i]['text']}"

        update.effective_message.reply_text(text["promo_displayed"],
                                            reply_markup=ReplyKeyboardRemove(),
                                            parse_mode='HTML')

        context.bot.send_chat_action(chat_id,
                                     action=ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(chat_id,
                               photo=open(
                                   promos[i]['image'][1:], 'rb'),
                               caption=promo_text,
                               reply_markup=InlineKeyboardMarkup(
                                   [
                                       [InlineKeyboardButton(
                                           button["like_it"],
                                           callback_data='like')],
                                       [InlineKeyboardButton(
                                           button["next"],
                                           callback_data='next')],
                                       [InlineKeyboardButton(
                                           button["back_to_main"],
                                           callback_data="exit")]
                                   ]
                               ),
                               parse_mode='HTML')

        logging.info(
            f"User {chat_id} has just started scrolling promo list. Returned state: {state}")
        return state

    def scrolling(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        query = update.callback_query
        toggler = [
            InlineKeyboardButton(
                button["previous"],
                callback_data='prev'),
            InlineKeyboardButton(
                button["next"],
                callback_data='next')
        ]
        if query.data == 'next':
            i = context.user_data['current_index'] + 1
        else:
            i = context.user_data['current_index'] - 1
        context.user_data.update(
            {
                'current_index': i
            }
        )
        next_display_id = context.user_data['promo_ids'][
            context.user_data['current_index']
        ]
        if next_display_id == context.user_data['last_promo']:
            toggler.pop()
        elif next_display_id == context.user_data['first_promo']:
            toggler.pop(0)
        promo = get(f"promo/{next_display_id}")
        promo_text = f"<b>{promo['name']}</b>\n\n{promo['text']}"

        query.answer()
        query.delete_message()
        context.bot.send_chat_action(chat_id,
                                     action=ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(chat_id,
                               photo=open(
                                   promo['image'][1:], 'rb'),
                               caption=promo_text,
                               reply_markup=InlineKeyboardMarkup(
                                   [
                                       [InlineKeyboardButton(
                                           button["like_it"],
                                           callback_data='like')],
                                       toggler,
                                       [InlineKeyboardButton(
                                           button["back_to_main"],
                                           callback_data="exit")]
                                   ]
                               ),
                               parse_mode='HTML')

    def like_it(self, update: Update, context: CallbackContext):
        pass

    def back_to_menu(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        query.delete_message()
        return Menu().display(update, context)
