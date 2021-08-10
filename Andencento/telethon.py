from telethon import TelegramClient

import os

TOKEN = os.environ.get("TOKEN", None)
NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, os.environ.get("APP_ID", None), os.environ.get("APP_HASH", None)
)

# Telethon
tbot.start(bot_token=TOKEN)
