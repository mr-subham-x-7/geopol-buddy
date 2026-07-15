import asyncio

from logger import setup_logger
from config import check_secrets
from gemini import test_connection
from telegram_client import send_test_message
from x.client import XClient
from x.fetch import TweetFetcher

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

    # Test X Login
    logger.info("🐦 Testing X authentication...")

    x_client = XClient()
    await x_client.login()

    logger.info("✅ X authentication successful!")

    # Test X Tweet Fetching
    logger.info("📰 Fetching tweets from X...")

    fetcher = TweetFetcher()

    tweets = await fetcher.fetch_user_tweets(
        username="Reuters",
        limit=5
    )

    for tweet in tweets:
        logger.info(tweet.rawContent)

    logger.info("✅ Tweet fetching successful!")

    logger.info("🎉 Geopol Buddy completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
