"""Example of the usage of EmotionsList"""
from examples.adt_realization.emotions_list import EmotionsList


print("File to train model:")
EMOTIONS_LIST = EmotionsList('NRC-Emotion-Intensity-Lexicon-v1.txt')
print(EMOTIONS_LIST.database)

print("\nTweet:")
TWEET = "I am very sad during the quarantine period"
EMOTIONS_LIST.set_tweet(TWEET)
print(EMOTIONS_LIST.tweet)

print("\nMain EMOTION of the TWEET:")
EMOTIONS_LIST.get_tweet_emotion()
print(EMOTIONS_LIST.emotions)

print("\nEmotions and their probabilities:")
EMOTIONS_LIST.get_emotions_probability()
print(EMOTIONS_LIST.probabilities)
