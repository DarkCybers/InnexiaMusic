import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION = getenv("SESSION", "session")
TOKEN = getenv("TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SiderzBot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c0602eaaad36db501652c.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "InnexiaAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SiderzChat")
PROJECT_NAME = getenv("PROJECT_NAME", "innexiaMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/DarkCybers/innexiaMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GROUP = getenv("LOG_GROUP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
