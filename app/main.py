import asyncio

from logger import setup_logger
from config import check_secrets
from gemini import test_connection
from telegram_client import send_test_message

logger = setup_logger()


def main():
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

    asyncio.run(send_test_message())

    logger.info("✅ Telegram message sent successfully!")

    logger.info("🎉 Geopol Buddy completed successfully!")


if __name__ == "__main__":
    main()
