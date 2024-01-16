class Node:
    """

    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list_string = ''
        current_node = self.head
        while current_node:
            current_node_string = current_node.__str__()
            linked_list_string += f'{{ {current_node_string} }} -> '
            current_node = current_node.next
        linked_list_string += 'NULL'
        return linked_list_string

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        pass

class TargetError:
    pass
