import json
from pathlib import Path


class Storage:
    """Handles reading and writing processed articles."""

    def __init__(self):
        self.file = Path("data/processed_articles.json")

    def load(self):
        """Load processed articles."""

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, articles):
        """Save processed articles."""

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                articles,
                f,
                indent=4,
                ensure_ascii=False,
            )
