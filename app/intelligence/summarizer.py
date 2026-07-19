from google import genai
from config import GEMINI_API_KEY


class Summarizer:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def test(self):
        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents="Reply with exactly: Geopol Buddy connected successfully!"
        )
        return response.text

    def summarize(self, articles):

        if not isinstance(articles, list):
            articles = [articles]

        context = ""

        for article in articles:
            context += f"""
Title: {article['title']}
Source: {article['source']}
Summary: {article['summary']}

"""

        prompt = f"""
You are a geopolitical intelligence analyst.

Analyze these related news reports as one event.

{context}

Produce:

1. What happened
2. Why it matters
3. Who is affected
4. Possible implications

Keep it under 250 words.
"""

        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        return response.text
