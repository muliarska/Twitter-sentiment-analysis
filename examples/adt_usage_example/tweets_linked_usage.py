"""Example of the usage of TweetsLinkedList"""
from examples.adt_realization.tweets_linked_list import TweetsLinkedList

TWEETS_LIST = TweetsLinkedList('realDonaldTrump')
TWEETS_LIST.create_linked()


print("Description of the user:")
CUR_NODE = TWEETS_LIST.data
print(CUR_NODE.data)
CUR_NODE = CUR_NODE.next


print("\nAll tweets and their dates:")
while CUR_NODE is not None:
    print(CUR_NODE.data)
    CUR_NODE = CUR_NODE.next


DAY = TWEETS_LIST.available_dates[0][1]
print("\nDay:")
print(DAY)
print("Tweets in that DAY:")
print(TWEETS_LIST.get_tweet_by_day(DAY))
