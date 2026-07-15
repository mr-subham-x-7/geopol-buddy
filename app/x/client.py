import os

from twscrape import API

from app logger import get_logger

logger = setup_logger()


class XClient:
    def __init__(self):
        self.api = API()
        logger.info("✅ twscrape API initialized")

    async def login(self):
        username = os.getenv("X_USERNAME")
        password = os.getenv("X_PASSWORD")
        email = os.getenv("X_EMAIL")

        await self.api.pool.add_account(
            username=username,
            password=password,
            email=email,
            email_password=password,
        )

        await self.api.pool.login_all()

        logger.info("✅ Successfully logged into X")

    def get_api(self):
        return self.api
