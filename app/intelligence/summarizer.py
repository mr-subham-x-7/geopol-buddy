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
You are a senior geopolitical intelligence analyst.

Analyze these related news reports as one geopolitical event.

{context}

Return EXACTLY in this format.

Severity:
(Low / Medium / High / Critical)

Confidence:
(Low / Medium / High)

Countries:
(country names)

Sources:
(source names only)

What happened:
(3-5 sentences)

Why it matters:
(2-4 sentences)

Who is affected:
(list)

Possible implications:
(2-4 bullet points)

Keep the entire response under 250 words.
Do not use Markdown.
Do not invent facts.
Only use information supported by the provided articles.
"""
        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        return response.text
