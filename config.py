## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzcBu1TY43W0guskp_UpBT3Rk5nuBHXPTDYWdEPsmJ-iI16wqo-IBz9lb2IjI54dIrBPxci_9I6STcL325Hd2G_9C0m9oDPTxOlZ8kH1XYMpgBEjW_brl1or83Mc7Y8C53xRRXjp_b_gx0npT0A7IOw8e8azlYPCo3NIcKUdm7B7NlTqyjry7NRlzob33yAHyo9ru3uD-tJNd0zW145GjZ90i_y_mwCHBAhKVZG_6DnMBfuPVOfAEYg83hd6EkhMyCDxHmRwZlZ13mXIsmC0LnIgbM2o1_LRb7wUTcpgwGVFAxa0qBYe6fmJJkZFyivOMO5P99Xcko8ssgw9N9TFFNrwBP4=")
BOT_TOKEN = getenv("BOT_TOKEN", "5103339944:AAFz_MvtMQ6rkKvAZIKixrG5HMjnICGzIEM")
BOT_NAME = getenv("BOT_NAME", "FrEeDoM Vid")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "مصطفى")
OWNER_USERNAME = getenv("OWNER_USERNAME", "mc312")
ALIVE_NAME = getenv("ALIVE_NAME", "مصطفى")
BOT_USERNAME = getenv("BOT_USERNAME", "mc3112bot")
OWNER_ID = getenv("OWNER_ID", "680747651")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "zvpzc")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "lrrttt")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "lrrttt")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "680747651").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
