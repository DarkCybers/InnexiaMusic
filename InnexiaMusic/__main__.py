import requests
from pyrogram import Client as Bot

from InnexiaMusic.config import API_HASH, API_ID, BG_IMAGE, TOKEN
from Innexia.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./image/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="plugins"),
)

bot.start()
run()
