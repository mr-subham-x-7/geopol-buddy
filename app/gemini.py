from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def test_connection():
    response = client.models.generate_content(
        model="gemini-2.5-pro-preview",
        contents="Reply with exactly: Geopol Buddy connected successfully!"
    )

    return response.text
