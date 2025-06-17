import asyncio
import importlib
import logging
import re
import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client

import config
from RAUSHAN.modules import all_modules

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous

OWNER = config.OWNER_ID

class AMBOT(Client):
    def __init__(self):
        super().__init__(
            name="AMBOT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="RAUSHAN.modules"),
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        self.name = get_me.mention
        self.username = get_me.username

    async def stop(self):
        await super().stop()

# Async helper to safely fetch bot info
async def init_dev_bot():
    dev = Client(
        "Dev",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    await dev.start()
    x = await dev.get_me()
    await dev.stop()

    return {
        "BOT_ID": x.id,
        "BOT_NAME": x.first_name + (x.last_name or ""),
        "BOT_USERNAME": x.username,
        "BOT_MENTION": x.mention,
        "BOT_DC_ID": getattr(x, "dc_id", None)
    }

bot_info = asyncio.run(init_dev_bot())

BOT_ID = bot_info["BOT_ID"]
BOT_NAME = bot_info["BOT_NAME"]
BOT_USERNAME = bot_info["BOT_USERNAME"]
BOT_MENTION = bot_info["BOT_MENTION"]
BOT_DC_ID = bot_info["BOT_DC_ID"]
