import tweepy
import logging

import credentials

consumer_key = credentials.API_key
consumer_secret_key = credentials.API_secret_key
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret
bearer_token = credentials.bearer_token
twitter_id = "1495212918614462473"

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token,
)

# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)


def get_last_tweet(file):
    f = open(file, "r")
    lastId = int(f.read().strip())
    f.close()
    return lastId


def put_last_tweet(file, Id):
    f = open(file, "w")
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")
    return


def respondToTweet(file="tweet_ID.txt"):
    last_id = get_last_tweet(file)
    response = client.get_users_mentions(twitter_id, since_id=last_id)
    mentions = response[0]
    if mentions == None:
        return

    new_id = 0
    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        logger.info(f"{mention.id} - {mention.text} ")
        new_id = mention.id

        try:
            logger.info("liking and replying to tweet")

            # TODO: Further logic here
            # client.create_favorite(mention.id)
            # client.update_status(
            #     "@" + mention.user.screen_name + " My response is here", mention.id
            # )
        except:
            logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)


if __name__ == "__main__":
    respondToTweet()
