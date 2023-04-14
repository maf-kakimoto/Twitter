import tweepy
import config

API_KEY = config.CONSUMER_KEY
API_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
all_tweets = []

latest_tweets = api.user_timeline(count=200, tweet_mode='extended')
all_tweets.extend(latest_tweets)

while len(latest_tweets) > 0:
    latest_tweets = api.user_timeline(count=200, max_id=all_tweets[-1].id-1, tweet_mode='extended')
    all_tweets.extend(latest_tweets)

with open('xxx', 'w', newline='') as f:
    for tweet in (reversed(all_tweets)):
        if tweet.full_text.startswith('xxx'):
            f.write(tweet.full_text)
            f.write('\n\n')
