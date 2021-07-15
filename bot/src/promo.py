from telegram import Update, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
from telegram.ext import CallbackContext
from bot.src.menu import Menu
from bot.utils.get_photo_id import get_photo_id
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
        promos = requests.get(
            API_URL + "promo", auth=API_AUTHENTICATION).json()
        if len(promos) == 0:
            update.effective_message.reply_text(
                "<b>Действующих акций пока нет 😔</b>", parse_mode='HTML')
            return
        promo_text = f"<b>{promos[0]['name']}</b>\n\n{promos[0]['text']}"
        promo_ids = []
        for i in promos:
            promo_ids.append(i['id'])
        context.user_data.update(
            {
                "current_promo_id": promos[0]['id']
            }
        )
        print(promo_ids)

        update.effective_message.reply_text(text["promo_displayed"],
                                            reply_markup=ReplyKeyboardRemove(),
                                            parse_mode='HTML')

        try:
            file_id = context.bot_data['product_' + str(promos[0]['id'])]
            context.bot.send_photo(chat_id,
                                   photo=file_id,
                                   caption=promo_text, parse_mode='HTML')
        except KeyError:
            context.bot.send_chat_action(chat_id,
                                         action=ChatAction.UPLOAD_PHOTO)
            msg = context.bot.send_photo(chat_id,
                                         photo=open(str(BASE_DIR) +
                                                    promos[0]['image'], 'rb'),
                                         caption=promo_text,
                                         reply_markup=InlineKeyboardMarkup(
                                             [
                                                 [InlineKeyboardButton(
                                                     button["like_it"], callback_data=1)],
                                                 [InlineKeyboardButton(
                                                     button["previous"], callback_data='prev'), InlineKeyboardButton(button["next"], callback_data='next')],
                                                 [InlineKeyboardButton(
                                                     button["back_to_main"], callback_data="exit")]
                                             ]
                                         ),
                                         parse_mode='HTML')
            # payload = {
            #     "promo_" + str(promos['id']): get_photo_id(msg.photo)
            # }
            # context.bot_data.update(payload)

        logging.info(
            f"User {chat_id} is watching promos. Returned state: {state}")
        return state

    def back_to_menu(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        query.delete_message()
        return Menu().display(update, context)

    def next(self, update: Update, context: CallbackContext):
        pass
