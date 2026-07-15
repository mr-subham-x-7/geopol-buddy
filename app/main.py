from logger import setup_logger
from config import check_secrets
from gemini import test_connection

logger = setup_logger()


def main():
    logger.info("🚀 Geopol Buddy starting...")

    missing = check_secrets()

    if missing:
        logger.error("❌ Missing GitHub Secrets:")
        for secret in missing:
            logger.error(f"   - {secret}")
        return

    logger.info("✅ All GitHub Secrets verified.")

    logger.info("🤖 Testing Gemini connection...")

    reply = test_connection()

    logger.info("Gemini replied:")
    logger.info(reply)

    logger.info("🎉 Gemini integration successful!")


if __name__ == "__main__":
    main()
