import os
from pyrogram import Client


api_id = os.getenv("TELEGRAM_API")
api_hash = os.getenv("TELEGRAM_HASH")

# app = Client("my_account", api_id, api_hash)

# app.start()
# app.send_message("me", "Привет, это я!")
# app.stop()

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Привет, это я!")
