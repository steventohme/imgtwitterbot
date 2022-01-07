import tweepy
import time
from imgfunctions import bw
import os

API_KEY = "XxQwdIWue2kxq6bOCniFl1Noa"
API_SECRET = "5WZB9xb7PFVW3h4CFzfS40y6LcAXapO2SjEcTp2MNWlzUpskpe"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAEgcXgEAAAAAwrG1icgYI1tX7jM6uLKic6nfywE%3DzNqbr9L1kvPFgvvA9FFfRDSYP9ygl2CUzjgpFLeQZqPo73UuZ1"
ACCESS_TOKEN = "1449748044644294657-ZLavMjfevTetYnJdCDPDfrWeT3Uo32"
ACCESS_SECRET = "rvuH3Ezw1xTRRk8FdMNdR1q7pkQjYTPLs70A6uKNuSeR9"

auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api = tweepy.API(auth)


FILE = 'last_seen_id.txt'

def retrieve_id(file_name):
    fn = open(file_name, 'r')
    last_seen_id = int(fn.read().strip())
    fn.close()
    return last_seen_id

def store_id(last_seen_id, file_name):
    fn = open(file_name, 'w')
    fn.write(str(last_seen_id))
    fn.close()
    return

def BW_function():
    print('Checking for tweets')
    last_seen_id = retrieve_id(FILE)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_id(last_seen_id,FILE)
        if 'media' in mention.entities:
            print('Image found')
            print()
            bw(mention.entities['media'][0]['media_url'])
            media = api.media_upload("img.jpg")
            api.update_status('@' + mention.user.screen_name,media_ids=[media.media_id])
            os.remove("img.jpg")

while True:
    BW_function()
    time.sleep(10)