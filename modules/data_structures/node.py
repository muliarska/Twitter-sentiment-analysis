"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""


class Node:
    """Represents ta Node"""
    def __init__(self, data, next_node=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next_node


class TwoWayNode(Node):
    """Represents ta TwoWayNode"""
    def __init__(self, data, previous=None, next_node=None):
        """Instantiates a TwoWayNode"""
        Node.__init__(self, data, next_node)
        self.previous = previous


# Just an empty link
NODE1 = None

# A node containing emotions and an empty link
NODE2 = Node("A", None)

# A node containing emotions and a link to node2
NODE3 = Node("B", NODE2)
