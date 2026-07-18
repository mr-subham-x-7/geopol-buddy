from pathlib import Path
import json


class Storage:
    """Simple JSON storage for processed articles."""

    def __init__(self):
        self.file = Path("data/processed_articles.json")

        self.file.parent.mkdir(exist_ok=True)

        if not self.file.exists():
            self.file.write_text("[]")

    def load(self):
        """Load processed article IDs."""

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, articles):
        """Save processed article IDs."""

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(articles, f, indent=4)
