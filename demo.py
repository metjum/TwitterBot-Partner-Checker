import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()
try:
    api.update_status("testing")
    print("tweeted")
except Exception as e:
    print(e)