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

    def summarize(self, article):
        prompt = f"""
You are a geopolitical intelligence analyst.

Analyze this news article and respond in exactly this format:

What happened:
- Briefly explain the event.

Why it matters:
- Explain why this event is strategically important.

Who is affected:
- Mention the main countries or organizations involved.

Possible implications:
- Mention likely short-term consequences.

Title:
{article["title"]}

Summary:
{article["summary"]}
"""

        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        return response.text
