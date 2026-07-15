import os


REQUIRED_SECRETS = [
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID",
    "GEMINI_API_KEY",
    "X_USERNAME",
    "X_PASSWORD",
    "X_EMAIL",
]


def check_secrets():
    missing = []

    for secret in REQUIRED_SECRETS:
        if not os.getenv(secret):
            missing.append(secret)

    return missing
