import feedparser

from .base import BaseCollector


class RSSCollector(BaseCollector):
    """Collector for RSS news feeds."""

    RSS_FEEDS = [
        "https://feeds.reuters.com/Reuters/worldNews",
    ]

    def fetch(self):
        """Fetch RSS data."""

        feeds = []

        for url in self.RSS_FEEDS:
            feed = feedparser.parse(url)
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