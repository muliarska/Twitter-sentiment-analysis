"""Representing EmotionsList ADT"""
from nltk.classify import NaiveBayesClassifier
from examples.modules_examples.nltk_example.stopwords import STOPWORDS
from modules.data_structures.arrays import DynamicArray


class EmotionsList:
    """Representing EmotionsList ADT that preserves
    emotions and their probabilities"""
    def __init__(self, database):
        """
        (str) ->
        Initialize database and creates two DynamicArray
        objects, and trains the model
        """
        self.database = database
        self.tweet = None
        self.emotions = DynamicArray()
        self.probabilities = DynamicArray()
        self._classifier = self._train_model()

    def set_tweet(self, tweet):
        """
        (str) ->
        Sets TWEET which the ADT will analyze
        """
        self.tweet = tweet

    @staticmethod
    def _remove_stop_words(tweet):
        """
        (str) -> str
        Returns TWEET with removed stop words
        """
        tokens_without_sw = ""
        for word in tweet.split():
            if not word.lower() in STOPWORDS:
                tokens_without_sw += word.lower() + " "
        return tokens_without_sw

    def _tweets_features(self, tweet):
        """
        (str) -> dict
        Additional method.
        Creates dictionary with TWEET to use it in the
        classifying this TWEET
        """
        tweet = self._remove_stop_words(tweet)
        return {'TWEET': tweet}

    def _creating_set(self):
        """
        () -> DynamicArray
        Returns an array to train model on it
        """
        result_set = DynamicArray()
        file = open(self.database, "r", encoding='utf-8')
        file.readline()
        for line in file:
            line = line.split('\t')
            first_el = self._tweets_features(line[0])
            result_set.append((first_el, line[1]))
        return result_set

    def _train_model(self):
        """
        () -> NaiveBayesClassifier
        Trains model with JSON_DATA
        """
        train_set = self._creating_set()
        return NaiveBayesClassifier.train(train_set)

    def get_tweet_emotion(self):
        """
        () -> str
        Returns a main EMOTION of the TWEET and
        adds to the array
        """
        label = self._classifier.classify(self._tweets_features(self.tweet))
        self.emotions.append(label)
        return label

    def get_emotions_probability(self):
        """
        () -> DynamicArray
        Returns an array with emotions of the TWEET
        and their probabilities and adds to the array
        """
        emotions = DynamicArray()
        probabilities = self._classifier.prob_classify(self._tweets_features(self.tweet))
        for sample in probabilities.samples():
            emotions.append((sample, probabilities.prob(sample)))
        self.probabilities.append(emotions)
        return emotions
