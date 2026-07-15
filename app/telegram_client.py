from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


async def send_test_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text="🚀 Hello! Geopol Buddy is now connected to Telegram."
    )
