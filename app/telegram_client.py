from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


async def send_message(message):
    """Send any message to Telegram."""

    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=message,
    )


async def send_test_message():
    """Send a test message."""

    await send_message(
        "🚀 Hello! Geopol Buddy is now connected to Telegram."
    )
