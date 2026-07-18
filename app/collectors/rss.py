import feedparser

from .accounts import RSS_FEEDS
from .base import BaseCollector


class RSSCollector(BaseCollector):
    """Collector for RSS news feeds."""

    def fetch(self):
        """Fetch RSS data."""

        feeds = []

        for source in RSS_FEEDS:
            print(f"\n===== {source['name']} =====")

            feed = feedparser.parse(source["url"])

            print("Feed title:", feed.feed.get("title", "No title"))
            print("Number of entries:", len(feed.entries))
            print("Bozo:", feed.bozo)

            if feed.bozo:
                print("Exception:", feed.bozo_exception)

            feeds.append(feed)

        return feeds

    def parse(self, raw_data):
        """Parse RSS data into a list of articles."""

        articles = []

        for feed in raw_data:
            for entry in feed.entries:
                article = {
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                }

                articles.append(article)

        return articles
