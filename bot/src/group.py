from telegram import Update
from telegram.ext import CallbackContext


class Group:

    def reply_to_user(self, update: Update, context: CallbackContext):
        try:
            if update.message.reply_to_message:

                response = update.message.text

                reply_id = update.message.reply_to_message.message_id

                user_id = context.bot_data[reply_id]

                reply = f"<b>Сизга менежер жавоб йўллади:</b>\n\n{response}"

                context.bot.send_message(chat_id=user_id,
                                         text=reply,
                                         parse_mode='HTML')
            else:
                pass
        except KeyError:
            update.effective_message.reply_text(
                'Хато! Бунга жавоб беролмайман. Сервердаги маълумотлар йўқолган бўлиши мумкин.')
