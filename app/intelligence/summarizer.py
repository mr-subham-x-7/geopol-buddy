from gemini import test_connection, summarize_article


class Summarizer:
    """Handles AI summarization."""

    def test(self):
        """Test Gemini through the summarizer."""
        return test_connection()

    def summarize(self, article):
        """Summarize one article."""

        return summarize_article(
            title=article["title"],
            summary=article["summary"],
        )
