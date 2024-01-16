class Node:
    """

    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        pass

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        pass

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        pass

class TargetError:
    pass
