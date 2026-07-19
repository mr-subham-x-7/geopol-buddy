import asyncio

from logger import setup_logger
from config import check_secrets
from intelligence.summarizer import Summarizer
from intelligence.filter import NewsFilter
from intelligence.priority import PriorityFilter
from intelligence.clustering import EventCluster
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
    priority = PriorityFilter()

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
    filterer = NewsFilter()
    clusterer = EventCluster()

    raw_data = rss.fetch()
    articles = rss.parse(raw_data)

    # Remove duplicate headlines
    articles = filterer.remove_duplicates(articles)

    # Group related articles
    clusters = clusterer.cluster(articles)

    logger.info("📁 Event clusters:")

    for name, items in clusters.items():
        logger.info(f"{name}: {len(items)} article(s)")

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

    # Keep only new articles inside each cluster
    new_clusters = {}

    for cluster_name, cluster_articles in clusters.items():
        filtered = [
            article for article in cluster_articles
            if article in new_articles
        ]

        if filtered:
            new_clusters[cluster_name] = filtered

    # Send one intelligence report per event cluster
    if new_clusters:

        logger.info("🛰️ Generating intelligence reports by event...")

        for cluster_name, cluster_articles in new_clusters.items():

            logger.info(
                f"📁 {cluster_name}: {len(cluster_articles)} article(s)"
            )

            summary = summarizer.summarize(cluster_articles)

            message = f"""🛰️ GEOPOL BUDDY

📁 Event: {cluster_name}

📰 Related Articles: {len(cluster_articles)}

🧠 Intelligence Assessment

{summary}
"""

            logger.info(f"📨 Sending {cluster_name} report...")

            await send_message(message)

            logger.info(f"✅ {cluster_name} report sent!")

    logger.info("✅ RSS collection successful!")

    logger.info("🎉 Geopol Buddy completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
