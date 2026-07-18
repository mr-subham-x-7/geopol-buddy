import asyncio

from logger import setup_logger
from config import check_secrets
from intelligence.summarizer import Summarizer
from telegram_client import send_test_message, send_message
from collectors.rss import RSSCollector
from storage.storage import Storage

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

    # Test Intelligence Layer
    logger.info("🧠 Testing Intelligence Layer...")

    summarizer = Summarizer()

    reply = summarizer.test()

    logger.info("Gemini replied:")
    logger.info(reply)

    logger.info("🎉 Intelligence Layer is working!")

    # Test Telegram
    logger.info("📨 Sending Telegram test message...")

    await send_test_message()

    logger.info("✅ Telegram message sent successfully!")

    # Test RSS Collection
    logger.info("📰 Testing RSS collector...")

    rss = RSSCollector()
    storage = Storage()

    raw_data = rss.fetch()
    articles = rss.parse(raw_data)

    processed = storage.load()

    new_articles = []

    for article in articles:
        if article["link"] not in processed:
            new_articles.append(article)
            processed.append(article["link"])

    storage.save(processed)

    logger.info(f"✅ Collected {len(articles)} articles.")
    logger.info(f"🆕 New articles: {len(new_articles)}")

    logger.info("Latest new headlines:")

    for article in new_articles:
        logger.info(article["title"])

    # Generate AI summary for the first new article
    if new_articles:
        logger.info("🧠 Generating AI summary...")

        summary = summarizer.summarize(new_articles[0])

        logger.info("AI Summary:")
        logger.info(summary)

        message = f"""📰 {new_articles[0]["title"]}

🧠 AI Summary

{summary}

🔗 {new_articles[0]["link"]}
"""

        logger.info("📨 Sending intelligence report to Telegram...")

        await send_message(message)

        logger.info("✅ Intelligence report sent!")

    logger.info("✅ RSS collection successful!")

    logger.info("🎉 Geopol Buddy completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
