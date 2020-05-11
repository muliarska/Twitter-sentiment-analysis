from nltk.classify import NaiveBayesClassifier
from stopwords import stopwords
from arrays import DynamicArray


class EmotionsList:
    def __init__(self, database):
        self.database = database
        self.tweet = None
        self.emotions = DynamicArray()
        self.probabilities = DynamicArray()

    def set_tweet(self, tweet):
        self.tweet = tweet

    @staticmethod
    def _remove_stop_words(tweet):
        tokens_without_sw = ""
        for word in tweet.split():
            if not word.lower() in stopwords:
                tokens_without_sw += word.lower() + " "
        return tokens_without_sw

    def _tweets_features(self, tweet):
        tweet = self._remove_stop_words(tweet)
        return {'tweet': tweet}

    def _creating_set(self):
        result_set = DynamicArray()
        file = open(self.database, "r", encoding='utf-8')
        line = file.readline()
        for line in file:
            line = line.split('\t')
            first_el = self._tweets_features(line[0])
            result_set.append((first_el, line[1]))
        return result_set

    def _train_model(self):
        train_set = self._creating_set()
        return NaiveBayesClassifier.train(train_set)

    def get_tweet_emotion(self):
        classifier = self._train_model()

        label = classifier.classify(self._tweets_features(self.tweet))
        self.emotions.append(label)
        return label

    def get_emotions_probability(self):
        emotions = DynamicArray()
        classifier = self._train_model()
        print("type")
        print(type(classifier))

        probabilities = classifier.prob_classify(self._tweets_features(self.tweet))

        for sample in probabilities.samples():
            emotions.append((sample, probabilities.prob(sample)))
        self.probabilities.append(emotions)
        return emotions

