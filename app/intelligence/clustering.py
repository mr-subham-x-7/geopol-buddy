class EventCluster:
    """Groups related geopolitical news."""

    KEYWORDS = [
        "china",
        "taiwan",
        "india",
        "pakistan",
        "russia",
        "ukraine",
        "usa",
        "us",
        "america",
        "israel",
        "iran",
        "thailand",
        "indonesia",
        "vietnam",
        "nato",
        "japan",
        "north korea",
        "south korea",
        "philippines",
        "myanmar",
        "bangladesh",
        "nepal",
        "bhutan",
        "sri lanka",
        "afghanistan",
        "yemen",
        "eu",
        "un",
    ]

    def cluster(self, articles):
        groups = {}

        for article in articles:
            title = article["title"].lower()

            key = "other"

            for keyword in self.KEYWORDS:
                if keyword in title:
                    key = keyword
                    break

            groups.setdefault(key, []).append(article)

        return groups
