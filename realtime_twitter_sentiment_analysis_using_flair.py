# -*- coding: utf-8 -*-
"""Realtime Twitter Sentiment Analysis using Flair.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R8rGwjWy9rmqDDggwo0ChnT7-Ms8QCao

install module
"""

!pip install tweepy
!pip install flair

"""configurations"""

bearer = "hidden"
consumer_key = "hidden"
consumer_secret = "hidden"
access_token = "hidden"
access_token_secret = "hidden"

"""inport modules"""

import tweepy
import re
import time

from flair.models import TextClassifier
from flair.data import Sentence

#initialize tweepy

api = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
api.get_me()

## get realtime tweets

response = api.search_recent_tweets('#virat')

tweets = response.data
for tweet in tweets:
  print(tweet.text)
  print('---------------------------------------------------------------------')

## preprocessing

def preprocess_text(text):
  # convert to lowercase
  text = text.lower()
  #remove user handle
  text = re.sub("@[\w]*", "", text)
  #remove links
  text = re.sub("http\S+", "", text)
  #remove digits and spl characters
  text = re.sub("[^a-zA-Z#]", " ", text)
  #remove RT
  text = re.sub("rt", "", text)
  #remove additional spaces
  text = re.sub("\s+", " ", text)

  return text

tweet.text

preprocess_text(tweet.text)

#create sentiment analysis function

classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
  sentence = Sentence(tweet)
  classifier.predict(sentence)
  return str(sentence.labels[0]).split()[-2:]

get_sentiment(tweet.text)

"""# realtime sentiments"""

## preprocessing

def preprocess_text(text):
  # convert to lowercase
  text = text.lower()
  #remove user handle
  text = re.sub("@[\w]*", "", text)
  #remove links
  text = re.sub("http\S+", "", text)
  #remove digits and spl characters
  text = re.sub("[^a-zA-Z#]", " ", text)
  #remove RT
  text = re.sub("rt", "", text)
  #remove additional spaces
  text = re.sub("\s+", " ", text)

  return text

#create sentiment analysis function

classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
  sentence = Sentence(tweet)
  classifier.predict(sentence)
  return str(sentence.labels[0]).split()[-2]

# get realtime sentiments

i = 0
n = 0
p = 0
for i in range (0,20):
  #get tweets (10)
  tweets = api.search_recent_tweets("#crypto").data

  for tweet in tweets:
    original_tweet = tweet.text
    clean_tweet = preprocess_text(original_tweet)
    sentiment = get_sentiment(clean_tweet)

    # print('-------------------------------------------------------------------')
    # print(original_tweet)
    # print('-------------------------------------------------------------------')
    # print('Sentiment : ', sentiment)
    # print('-------------------------------------------------------------------')
    # #time.sleep(1)
    # print('\n\n')

    if sentiment == "POSITIVE":
      p=p+1
    else:
      n=n+1

  i=i+1


print('-------------------------------------------------------------------')
print("Positive Count : ",p,i)
print("Negative Count : ",n)
print('-------------------------------------------------------------------')
print("Positivity Rate : ",p/(i/10),"%")
print('-------------------------------------------------------------------')
