from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "28164938"))
API_HASH = getenv("API_HASH", "d53fd90b87686f713f6adc9428bbb6bb")
BOT_TOKEN = getenv("BOT_TOKEN", "7943558810:AAEvJS6_Am-jEGjS-d4Mj8OeOTlw7TdMlp0")
OWNER_ID = int(getenv("OWNER_ID", "5536473064"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://iamnobita1:nobitamusic1@cluster0.k08op.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUPPORT_GRP = getenv("SUPPORT_GRP", "OG_DEFAULTERS_01")
UPDATE_CHNL = getenv("UPDATE_CHNL", "NOBITA_MUSIC_SUPPORT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_NOBITA_DEFAULTERS_ll")

# Random Start Images
IMG = [
    "https://iili.io/FCghwJt.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgEAAxkBAAIJomRdLhVJVebkx0JRsp1STwTv3t3eAAJrAgAClpxhRD4z4bgqlIF0LwQ",
    "CAACAgUAAxkBAAIJo2RdLhjLjCpmPipMT8ksrqwUjGAIAAK1BQACLZ8oVFVNmhalU8eOLwQ",
    "CAACAgUAAxkBAAIJpGRdLkpU7t2WDj9zUFgCJ5uHUdGHAALTBAAC59CYV3t9x-f0tt4OLwQ",
]


EMOJIOS = [
    "❤️‍🔥",
    "🔥",
    "⚡️",
    "😎",
    "🌩",
    "🌦",
    "☀️",
    "💫",
]
