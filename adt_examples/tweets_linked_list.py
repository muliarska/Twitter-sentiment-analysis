from node import TwoWayNode
import json
from arrays import Array, DynamicArray


class TweetsLinkedList:
    def __init__(self, json_data):
        self.json = json_data
        self.data = None

    def _get_tweet_text(self, data, numb):
        return data['statuses'][numb]['text']

    def _get_created_at(self, data, numb):
        return data['statuses'][numb]['created_at']

    def _get_user_description(self, data, numb):
        return data['statuses'][numb]['user']['description']

    def create_linked(self):
        data = json.loads(self.json)
        # print(emotions)

        # node_array = Array(3)
        # node_array[0] = self._get_created_at(emotions, 0)
        # node_array[1] = self._get_tweet_text(emotions, 0)
        # node_array[2] = self._get_user_description(emotions, 0)

        node_array = Array(1)
        node_array[0] = self._get_user_description(data, 0)
        head = TwoWayNode(node_array)
        tail = head

        for i in range(1, len(data['statuses'])):
            node_array = Array(2)
            node_array[0] = self._get_created_at(data, i)
            node_array[1] = self._get_tweet_text(data, i)
            # node_array[2] = self._get_user_description(emotions, i)

            node = TwoWayNode(node_array)

            tail.next = node
            node.previous = tail
            tail = tail.next

        self.data = head

    @property
    def available_dates(self):
        available_dates = DynamicArray()
        cur_node = self.data.next
        while cur_node is not None:
            available_dates.append(cur_node[0])
            cur_node = cur_node.next
        return available_dates

    def get_tweet_by_day(self, day):
        assert day in self.available_dates, "This week is not available"
        days = DynamicArray()
        cur_node = self.data.next
        while cur_node is not None:
            if cur_node.data[0] == day:
                days.append((cur_node.data[1], cur_node.data[2]))
            cur_node = cur_node.next
        return days
