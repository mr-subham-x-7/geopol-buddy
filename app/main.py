 from logger import setup_logger
from config import check_secrets

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
    logger.info("🤖 Ready for API integrations.")
    logger.info("🎉 Foundation completed successfully!")


if __name__ == "__main__":
    main()
