class EventCluster:
    """Groups related news articles."""

    def cluster(self, articles):
        """Group articles by the first word of the title."""

        groups = {}

        for article in articles:
            title = article["title"].split()

            if not title:
                continue

            key = title[0].lower()

            groups.setdefault(key, []).append(article)

        return groups
