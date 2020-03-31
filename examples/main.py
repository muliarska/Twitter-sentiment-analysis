"""Represents an example of using Twitter API"""
import urllib.request
import urllib.error
import json
import ssl
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

ACCT = 'elonmusk'
URL = twurl.augment(TWITTER_URL,
                    {'q': ACCT, 'result_type': 'mixed', 'count': '10'})
CONNECTION = urllib.request.urlopen(URL, context=CTX)
DATA = CONNECTION.read().decode()

JS = json.loads(DATA)
with open('tweets.json', 'w', encoding="utf-8") as f:
    json.dump(JS, f, indent=2, ensure_ascii=False)

print("Tweets of Elon Musk:\n")
NUMBER = 1
for el in JS["statuses"]:
    print(str(NUMBER) + ".", el["text"])
    NUMBER += 1