
import random
import tweepy
#import_credentials
import time
import os
from dotenv import load_dotenv

load_dotenv()
#environment variables


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


def get_random_quote():
    return random_line('test.txt')

def create_tweet():
    quote = get_random_quote()
    print(quote)
    tweet = quote
    return tweet


API_KEY=os.getenv("API_KEY")
API_SECRET_KEY=os.getenv("API_SECRET_KEY")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")

consumer_key = API_KEY
consumer_secret_key = API_SECRET_KEY
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

def tweet_quote():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    test_tweet = create_tweet()
    api.update_status(test_tweet)
if __name__ == "__main__":
    tweet_quote()
    
def tweet_quote():
    interval = 60 * 60 * 6
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    while True:
        print('getting a random quote...')        
        tweet = create_tweet()
        api.update_status(tweet)
        time.sleep(interval)
    
        
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
bot_id= int(api.me().id_str)
mention_id=1
message=create_tweet()
while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("mention tweet found!")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id=mention.id
        if mention.in_reply_to_status_id is None and mention.author.id!=bot_id:
            name=mention.author.screen_name
            message=create_tweet()
            reply_tweet = "@" + str(name) + " " + message
            api.update_status(reply_tweet ,in_reply_to_status_id=mention.id_str)            
            print("Succesfully Replied")
    time.sleep(15)
        
