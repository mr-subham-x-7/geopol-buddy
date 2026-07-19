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

Return EXACTLY in the following format.

Severity:
Use exactly one of:
🟢 Low
🟡 Medium
🟠 High
🔴 Critical

Confidence:
Use exactly one of:
🟢 Low
🟡 Medium
🔴 High

Countries:
List all countries involved, separated by commas.

Sources:
Only list the news organizations used from the provided articles.

What happened:
(3–5 concise sentences)

Why it matters:
(2–4 concise sentences)

Who is affected:
(Bullet list)

Possible implications:
(Bullet list with 2–4 points)

Rules:
- Keep the entire response under 250 words.
- Do not use Markdown.
- Do not invent facts.
- Only use information supported by the provided articles.
- If information is uncertain, state that it is uncertain.
"""

        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        return response.text
