import os
import sys
import tweepy as tw

#defining keys
consumer_key= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

class MyStreamListener(tw.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, status):
        is_retweet = False
        if hasattr(status, "retweeted_status"):
            is_retweet = True
        if not is_retweet:
            if hasattr(status, "extended_tweet"):
                text = status.extended_tweet["full_text"]
            else:
                text = status.text
            print(status.user.name)
            print(text)
            api.retweet(status.id)


    def on_error(self, status_code):
        print("Erro encontrado (", status_code, ")")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

myStreamListener = MyStreamListener(api)
myStream = tw.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['celular xiaomi'])