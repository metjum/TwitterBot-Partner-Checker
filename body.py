
from email import message
from unicodedata import name
import requests 
import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()


def make_a_tweet(api):
    # Below are the hashtags that we target now. you can add or remove hashtags to this list in the format given below
    accounts=["@Streamerbans"] 
    user=random.choice(accounts)
    tweets = api.user_timeline(screen_name =random.choice(accounts) , count =2)
    
    for tweet in tweets:
        time.sleep(120)
        names=""
        s=False
        for i in tweet.text:
            if s:
                names = names + i
            if i == '"':
                if s:
                    break
                else:
                    s = True
        names = names[:-1]
        print(names)
        url = "https://api.ivr.fi/twitch/resolve/" + names
        resp = requests.get(url)
        resp = resp.json()
        message = names + " 🔨Partner: " + str(resp['partner'])
        print(message)
        try:
            tweet.favorite()
            time.sleep(20)
            api.update_status(message, in_reply_to_status_id = tweet.id,auto_populate_reply_metadata=True)
            print("done")
        except Exception as e:
            print(e)
            break



while True:
    print("inside the main function \n")
    make_a_tweet(api)
    time.sleep(5*60)
   
    print("......taking a break.....\n\n")
print('\n\n\n                   out of loop                          ')
