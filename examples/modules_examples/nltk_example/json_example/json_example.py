"""Example of json module"""
import urllib.request
import urllib.error
import ssl
import json
from examples.api_example import twurl


def generate_data(nickname):
    """
    (str) -> dict
    Returns a dictionary with information about the user's tweets
    """
    twitter_url = 'https://api.twitter.com/1.1/search/tweets.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    acct = nickname
    url = twurl.augment(twitter_url,
                        {'q': acct, 'result_type': 'mixed', 'count': '50'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    jsonn = json.loads(data)
    return jsonn


if __name__ == '__main__':
    JSON_DATA = generate_data('elonmusk')
    print("Tweets and retweets of the user (elonmusk):\n")
    for element in JSON_DATA['statuses']:
        print(element['text'])
