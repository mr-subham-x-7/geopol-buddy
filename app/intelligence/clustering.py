class EventCluster:
    """Groups related geopolitical news into meaningful events."""

    EVENTS = {
        "China–Taiwan Tensions": [
            "china",
            "taiwan",
            "beijing",
            "taipei",
            "pla",
        ],
        "India–Pakistan Relations": [
            "india",
            "pakistan",
            "kashmir",
            "loc",
        ],
        "Russia–Ukraine Conflict": [
            "russia",
            "ukraine",
            "moscow",
            "kyiv",
        ],
        "Middle East Escalation": [
            "israel",
            "iran",
            "gaza",
            "hamas",
            "hezbollah",
            "lebanon",
            "syria",
            "iraq",
            "yemen",
            "houthi",
            "gulf",
            "hormuz",
        ],
        "US Foreign Policy": [
            "usa",
            "us",
            "america",
            "washington",
            "white house",
            "trump",
            "state department",
            "pentagon",
        ],
        "Korean Peninsula": [
            "north korea",
            "south korea",
            "kim jong",
            "seoul",
            "pyongyang",
        ],
        "Japan Security": [
            "japan",
            "tokyo",
        ],
        "South China Sea": [
            "south china sea",
            "philippines",
            "thailand",
            "indonesia",
            "vietnam",
        ],
        "South Asia": [
            "bangladesh",
            "nepal",
            "bhutan",
            "sri lanka",
            "myanmar",
            "afghanistan",
        ],
        "Europe & NATO": [
            "nato",
            "eu",
            "europe",
            "france",
        ],
        "Global Economy": [
            "imf",
            "world bank",
            "inflation",
            "oil",
            "trade",
            "tariff",
            "economy",
            "gdp",
            "interest rate",
        ],
        "Climate & Disaster": [
            "earthquake",
            "cyclone",
            "storm",
            "flood",
            "wildfire",
            "heatwave",
            "imd",
        ],
        "Space & Technology": [
            "isro",
            "nasa",
            "esa",
            "spacex",
            "satellite",
            "rocket",
            "ai",
            "artificial intelligence",
            "semiconductor",
            "chip",
            "tsmc",
            "nvidia",
            "asml",
        ],
    }

    def cluster(self, articles):
        groups = {}

        for article in articles:

            text = (
                article["title"] + " " +
                article.get("summary", "")
            ).lower()

            event = "General International News"

            for event_name, keywords in self.EVENTS.items():

                if any(keyword in text for keyword in keywords):
                    event = event_name
                    break

            groups.setdefault(event, []).append(article)

        return groups
