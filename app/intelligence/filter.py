class NewsFilter:
    """Filters duplicate news articles."""

    def remove_duplicates(self, articles):
        seen = set()
        unique = []

        for article in articles:
            title = article["title"].strip().lower()

            if title not in seen:
                seen.add(title)
                unique.append(article)

        return unique
