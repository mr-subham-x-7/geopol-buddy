from .base import BaseCollector


class RSSCollector(BaseCollector):
    """Collector for RSS news feeds."""

    def fetch(self):
        """Fetch RSS data."""
        pass

    def parse(self, raw_data):
        """Parse RSS data."""
        pass