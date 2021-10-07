import os
from telegram.ext import Updater, Filters, MessageHandler

bot_token = os.getenv("BOT_TOKEN")

updater = Updater(token=bot_token)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я KittyBot!")


updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling(poll_interval=20.0)
updater.idle()
