class EventCluster:
    """Groups related geopolitical news."""

    KEYWORDS = [
        # Countries / Regions
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
        "japan",
        "thailand",
        "vietnam",
        "indonesia",
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

        # Organizations
        "nato",
        "un",
        "eu",

        # Event types
        "earthquake",
        "missile",
        "war",
        "strike",
        "attack",
        "military",
        "defence",
        "navy",
        "army",
        "air force",
        "drone",
        "cyber",
        "tariff",
        "trade",
        "sanction",
        "economy",
        "rocket",
        "satellite",
        "space",
        "currency",
        "investment",
        "finance",
        "typhoon",
    ]

    def cluster(self, articles):
        groups = {}

        for article in articles:
            title = article["title"].lower()

            key = "other"

            for keyword in self.KEYWORDS:
                if keyword in title:
                    key = keyword.title()
                    break

            groups.setdefault(key, []).append(article)

        return groups
