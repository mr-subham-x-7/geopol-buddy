from twscrape import API
from app.logger.logger import get_logger

logger = get_logger(__name__)


class XClient:
    def __init__(self):
        self.api = API()
        logger.info("✅ twscrape API initialized")

    def get_api(self):
        return self.api
