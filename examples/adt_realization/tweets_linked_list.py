"""Representing a TweetsLinkedList ADT"""
from modules.data_structures.node import TwoWayNode
from examples.api_example.api_example import generate_data
from modules.data_structures.arrays import Array, DynamicArray


class TweetsLinkedList:
    """Representing a TweetsLinkedList ADT based on
    linked structure"""
    def __init__(self, nickname):
        """
        (str) ->
        Initialize JSON_DATA from Twitter API and linked structure
        to keep information about tweets
        """
        self.json = generate_data(nickname)
        self.data = None

    @staticmethod
    def _get_tweet_text(data, numb):
        """
        (dict, int) -> str
        Returns text of the TWEET by the given number
        """
        try:
            return data['statuses'][numb]['text']
        except IndexError:
            return None

    @staticmethod
    def _get_created_at(data, numb):
        """
        (dict, int) -> str
        Returns date of the TWEET when it was created at
        by the given number
        """
        try:
            return data['statuses'][numb]['created_at']
        except IndexError:
            return None

    @staticmethod
    def _get_user_description(data, numb):
        """
        (dict, int) -> str
        Returns text of the user description by the specified number
        """
        try:
            return data['statuses'][numb]['user']['description']
        except IndexError:
            return None

    def create_linked(self):
        """
        () ->
        Creates linked structure in which each node stores
        the text and date of the TWEET, and in the first node
        a description of the user
        """
        node_array = Array(1)
        node_array[0] = self._get_user_description(self.json, 0)
        head = TwoWayNode(node_array)
        tail = head

        for i in range(1, len(self.json['statuses'])):
            node_array = Array(2)
            node_array[0] = self._get_created_at(self.json, i)
            node_array[1] = self._get_tweet_text(self.json, i)

            node = TwoWayNode(node_array)

            tail.next = node
            node.previous = tail
            tail = tail.next

        self.data = head

    @property
    def available_dates(self):
        """
        () -> DynamicArray
        Returns a list with the dates on which user wrote tweets
        """
        available_dates = DynamicArray()
        cur_node = self.data.next
        while cur_node is not None:
            try:
                date = cur_node.data[0].split()
                day = "{} {} {}".format(date[1], date[2], date[5])
                available_dates.append((cur_node.data[0], day))
                cur_node = cur_node.next
            except IndexError:
                pass
        return available_dates

    def get_tweet_by_day(self, day):
        """
        (str) -> DynamicArray
        Returns a list of tweets that have been written
        at given DAY
        """
        counter = False
        for date in self.available_dates:
            if date[1] == day:
                day = date[0]
                counter = True

        if not counter:
            raise ValueError("This DAY is not available")

        days = DynamicArray()
        cur_node = self.data.next
        while cur_node is not None:
            if cur_node.data[0] == day:
                days.append(cur_node.data[1])
            cur_node = cur_node.next
        return days
