"""Example of nltk module"""
from nltk.classify import NaiveBayesClassifier
from examples.modules_examples.nltk_example.stopwords import STOPWORDS
from modules.data_structures.arrays import DynamicArray


def remove_stop_words(tweet):
    """
    (str) -> str
    Returns TWEET with removed stop words
    """
    tokens_without_sw = ""
    for word in tweet.split():
        if not word.lower() in STOPWORDS:
            tokens_without_sw += word.lower() + " "
    return tokens_without_sw


def tweets_features(tweet):
    """
    (str) -> dict
    Creates dictionary with TWEET to use it in the
    classifying this TWEET
    """
    tweet = remove_stop_words(tweet)
    return {'TWEET': tweet}


def creating_set(database):
    """
    () -> DynamicArray
    Returns an array to train model on it
    """
    result_set = DynamicArray()
    file = open(database, "r", encoding='utf-8')
    file.readline()
    for line in file:
        line = line.split('\t')
        first_el = tweets_features(line[0])
        result_set.append((first_el, line[1]))
    return result_set


def train_model(database):
    """
    () -> NaiveBayesClassifier
    Trains model with JSON_DATA
    """
    train_set = creating_set(database)
    return NaiveBayesClassifier.train(train_set)


def get_emotions(tweet):
    """
    (str) -> list, str
    Returns a list with all emotions and their probabilities
    and a main EMOTION of the tweet
    """
    classifier = train_model('NRC-Emotion-Intensity-Lexicon-v1.txt')

    emotions = []
    probabilities = classifier.prob_classify(tweets_features(tweet))
    for sample in probabilities.samples():
        emotions.append((sample, probabilities.prob(sample)))

    label = classifier.classify(tweets_features(tweet))

    return emotions, label


if __name__ == '__main__':
    TWEET = "It was one of the best years of my life! Although there were difficulties sometimes."
    print("Tweet:")
    print(TWEET)

    EMOTIONS_LIST, LABEL = get_emotions(TWEET)

    print("\nMain EMOTION of the tweet:")
    print(LABEL)

    print("\nEmotions and their probabilities:")
    print(EMOTIONS_LIST)
