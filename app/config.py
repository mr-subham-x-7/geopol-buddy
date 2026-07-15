import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

REQUIRED_SECRETS = [
    "GEMINI_API_KEY",
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID",
]


def check_secrets():
    missing = []

    for secret in REQUIRED_SECRETS:
        if not os.getenv(secret):
            missing.append(secret)

    return missing
