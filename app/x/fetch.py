from x.client import XClient
from logger import setup_logger

logger = setup_logger()


class TweetFetcher:

    def __init__(self):
        self.client = XClient()

    async def fetch_user_tweets(self, username, limit=5):
        api = self.client.get_api()

        tweets = []

        async for tweet in api.user_tweets(username, limit=limit):
            tweets.append(tweet)

        logger.info(
            f"✅ Fetched {len(tweets)} tweets from @{username}"
        )

        return tweets
