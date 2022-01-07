import tweepy
import time
from imgfunctions import bw
import os

API_KEY = ""
API_SECRET = ""
BEARER_TOKEN = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# Set up API environment
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api = tweepy.API(auth)

#setting up file with the last tweet parsed, so tweets are not repeated.
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

# looks for files that mention the account and checks if they tweeted an image. The image is then ran through 
#a function called bw which converts the image to black and white.
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
