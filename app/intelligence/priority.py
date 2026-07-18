class PriorityFilter:
    """Ranks articles by geopolitical importance."""

    KEYWORDS = {
        "china": 5,
        "taiwan": 5,
        "india": 5,
        "pakistan": 5,
        "russia": 5,
        "ukraine": 5,
        "iran": 5,
        "israel": 5,
        "north korea": 5,
        "south korea": 4,
        "japan": 4,
        "military": 4,
        "army": 4,
        "navy": 4,
        "air force": 4,
        "missile": 4,
        "war": 4,
        "border": 3,
        "sanctions": 3,
        "trade": 3,
        "tariff": 3,
        "cyber": 3,
        "terror": 3,
        "earthquake": 2,
        "flood": 2,
        "wildfire": 2,
    }

    def score(self, article):
        score = 0

        text = (
            article.get("title", "") + " " +
            article.get("summary", "")
        ).lower()

        for keyword, value in self.KEYWORDS.items():
            if keyword in text:
                score += value

        article["score"] = score
        return score

    def select_top(self, articles, limit=3):
        for article in articles:
            self.score(article)

        ranked = sorted(
            articles,
            key=lambda x: x["score"],
            reverse=True,
        )

        return ranked[:limit]
