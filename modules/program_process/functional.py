"""Represents a class Functional"""
from modules.twitter_list_adt.tweets_linked_list import TweetsLinkedList
from modules.emotion_list.emotions_list import EmotionsList


class Functional:
    """Manages a process of the program_process"""
    def __init__(self):
        """
        () ->
        Initialize an emotions_list, a tweets_list and a nickname
        to facilitate the management of program processes
        """
        self.emotions_list = EmotionsList('NRC-Emotion-Intensity-Lexicon-v1.txt')
        self.tweets_list = None
        self.nickname = None

    def set_nickname(self, nickname):
        """
        (str) ->
        Sets nickname of the user with which the program works
        """
        self.nickname = nickname
        self.tweets_list = TweetsLinkedList(nickname)
        self.tweets_list.create_linked()

    @staticmethod
    def _two_emotions(emotions):
        """
        (list) -> list
        Returns a list divided into positive and negative
        emotions with their probabilities
        """
        prob1 = (emotions[4][1] + emotions[6][1] + emotions[7][1]) / 3
        prob2 = (emotions[0][1] + emotions[2][1] + emotions[3][1] + emotions[5][1]) / 4
        probability1 = prob1 / (prob1 + prob2)
        probability2 = 1 - probability1

        return [('positive', probability1), ('negative', probability2)]

    def available_days(self):
        """
        () -> list
        Returns a list with the dates on which user wrote tweets
        """
        dates = []
        for date in self.tweets_list.available_dates:
            if date[1] not in dates and len(dates) < 10:
                dates.append(date[1])
        return dates

    def many_emotions_last_time(self):
        """
        () -> list
        Returns a list with emotions and their probabilities
        for last time
        """
        result = []
        for i in range(8):
            cur_node = self.tweets_list.data
            name = None
            probability = 0
            counter = 0
            while cur_node is not None and counter < 20:
                if len(cur_node.data) == 1:
                    text = cur_node.data[0]
                else:
                    text = cur_node.data[1]
                self.emotions_list.set_tweet(text)
                emotions_tuple = self.emotions_list.get_emotions_probability()[i]
                name = emotions_tuple[0]
                probability += emotions_tuple[1]
                cur_node = cur_node.next
                counter += 1
            result.append((name, probability / counter))
        return result

    def two_emotions_last_time(self):
        """
        () -> list
        Returns a list divided into positive and negative
        emotions with their probabilities for last time
        """
        emotions = self.many_emotions_last_time()
        return self._two_emotions(emotions)

    def many_emotions_specific_day(self, day):
        """
        (str) -> list
        Returns a list with emotions and their probabilities
        for a specific day
        """
        result = []
        tweets = self.tweets_list.get_tweet_by_day(day)

        for i in range(8):
            name = None
            probability = 0
            counter = 0
            for text in tweets:
                while counter < 20:
                    self.emotions_list.set_tweet(text)
                    emotions_tuple = self.emotions_list.get_emotions_probability()[i]
                    name = emotions_tuple[0]
                    probability += emotions_tuple[1]
                    counter += 1
            result.append((name, probability / counter))
        return result

    def two_emotions_specific_day(self, day):
        """
        (str) -> list
        Returns a list divided into positive and negative
        emotions with their probabilities for a specific day
        """
        emotions = self.many_emotions_specific_day(day)
        return self._two_emotions(emotions)

    @staticmethod
    def _one_emotion(emotions_lst, emotion):
        """
        (list, str) -> tuple
        Returns the emotion and its probability
        """
        for cur_el in emotions_lst:
            if cur_el[0] == emotion:
                return cur_el
        return None

    def one_emotion_last_time(self, emotion):
        """
        (str) -> tuple
        Returns the emotion and its probability for last time
        """
        return self._one_emotion(self.many_emotions_last_time(), emotion)

    def one_emotion_specific_day(self, emotion, day):
        """
        (str) -> tuple
        Returns the emotion and its probability for a specific day
        """
        return self._one_emotion(self.many_emotions_specific_day(day), emotion)
