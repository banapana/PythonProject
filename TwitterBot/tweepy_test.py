import tweepy
import datetime

consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = ""
access_token_secret = ""

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#트윗 포스트하기
tweet = str(datetime.datetime.now()) + ' Brain Python Test.'
api.update_status(status=tweet)

print("Successfully Posted.")
print()

# 타임 라인 읽어오기
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)