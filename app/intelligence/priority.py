class PriorityFilter:
    """Selects the most important articles."""

    KEYWORDS = [
        "china",
        "taiwan",
        "india",
        "pakistan",
        "russia",
        "ukraine",
        "israel",
        "japan",
        "south korea",
        "nato",
        "military",
        "missile",
        "war",
        "attack",
        "border",
        "sanctions",
        "navy",
        "air force",
        "army",
    ]

    def score(self, article):
        score = 0

        title = article["title"].lower()

        for keyword in self.KEYWORDS:
            if keyword in title:
                score += 1

        return score

    def select_top(self, articles, limit=3):
        return sorted(
            articles,
            key=self.score,
            reverse=True
        )[:limit]
