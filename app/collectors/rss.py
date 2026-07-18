import feedparser

from .accounts import RSS_FEEDS
from .base import BaseCollector


class RSSCollector(BaseCollector):
    """Collector for RSS news feeds."""

    def fetch(self):
        """Fetch RSS data."""

        feeds = []

        for source in RSS_FEEDS:
            feed = feedparser.parse(source["url"])
            feeds.append(feed)

        return feeds

    def parse(self, raw_data):
        """Parse RSS data into a list of articles."""

        articles = []

        for feed in raw_data:
            source = feed.feed.get("title", "Unknown Source")

            for entry in feed.entries:
                article = {
                    "source": source,
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                }

                articles.append(article)

        articles.sort(
            key=lambda article: article.get("published", ""),
            reverse=True,
        )

        return articles
