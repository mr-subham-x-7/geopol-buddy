from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def test_connection():
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="Reply with exactly: Geopol Buddy connected successfully!"
    )
    return response.text


def summarize_article(title, summary):
    """Summarize a news article."""

    prompt = f"""
You are a geopolitical intelligence analyst.

Summarize this news article in 3-5 concise sentences.

Title:
{title}

Content:
{summary}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text
