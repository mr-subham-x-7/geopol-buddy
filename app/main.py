import asyncio

from logger import setup_logger
from config import check_secrets
from gemini import test_connection
from telegram_client import send_test_message
from collectors.rss import RSSCollector

logger = setup_logger()


async def main():
    logger.info("🚀 Geopol Buddy starting...")

    # Check GitHub Secrets
    missing = check_secrets()

    if missing:
        logger.error("❌ Missing GitHub Secrets:")
        for secret in missing:
            logger.error(f"   - {secret}")
        return

    logger.info("✅ All GitHub Secrets verified.")

    # Test Gemini
    logger.info("🤖 Testing Gemini connection...")

    reply = test_connection()

    logger.info("Gemini replied:")
    logger.info(reply)

    logger.info("🎉 Gemini integration successful!")

    # Test Telegram
    logger.info("📨 Sending Telegram test message...")

    await send_test_message()

    logger.info("✅ Telegram message sent successfully!")

    # Test RSS Collection
    logger.info("📰 Testing RSS collector...")

    rss = RSSCollector()

    raw_data = rss.fetch()

    articles = rss.parse(raw_data)

    logger.info(f"✅ Collected {len(articles)} articles.")

    logger.info("Latest headlines:")

    for article in articles:
        logger.info(article["title"])

    logger.info("✅ RSS collection successful!")

    logger.info("🎉 Geopol Buddy completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
