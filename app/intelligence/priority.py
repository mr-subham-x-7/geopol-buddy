class PriorityFilter:
    """Ranks articles by geopolitical importance."""

    KEYWORDS = {
        "china": 5,
        "taiwan": 5,
        "india": 4,
        "pakistan": 4,
        "russia": 5,
        "ukraine": 5,
        "israel": 5,
        "iran": 5,
        "military": 5,
        "missile": 5,
        "war": 5,
        "border": 4,
        "sanctions": 4,
        "nato": 4,
        "un": 3,
    }

    def score(self, article):
        """Calculate a priority score."""

        title = article["title"].lower()

        score = 0

        for keyword, value in self.KEYWORDS.items():
            if keyword in title:
                score += value

        return score

    def select(self, articles):
        """Return the highest priority article."""

        if not articles:
            return None

        return max(articles, key=self.score)
