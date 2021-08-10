import logging
import os
from pyrogram import Client

TOKEN = os.get.environ("TOKEN", required=True)
APP_ID = os.get.environ("APP_ID", required=True)
APP_HASH = os.get.environ("APP_HASH", required=True)
session_name = TOKEN.split(":")[0]
pbot = Client(
    session_name,
    api_id=APP_ID,
    api_hash=APP_HASH,
    bot_token=TOKEN,
)

# disable logging for pyrogram [not for ERROR logging]
logging.getLogger("pyrogram").setLevel(level=logging.ERROR)

pbot.start()
