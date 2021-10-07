import os
import requests

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
URL = "https://api.thecatapi.com/v1/images/search"

updater = Updater(token=bot_token)


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get("url")
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([["/newcat"]], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=f"Привет, {name}. Посмотри, какого котика я тебе нашёл",
        reply_markup=button,
    )

    context.bot.send_photo(chat.id, get_new_image())


updater.dispatcher.add_handler(CommandHandler("start", wake_up))
updater.dispatcher.add_handler(CommandHandler("newcat", new_cat))
updater.start_polling(poll_interval=10.0)
updater.idle()
