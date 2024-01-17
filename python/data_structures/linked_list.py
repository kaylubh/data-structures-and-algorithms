class Node:
    """
    Represents a node in a singly linked list. Intended to be used with the LinkedList class which will instantiate nodes.

    Attributes:
      value (any): the value or data stored in the node
      next (node object, default = None): the next node in the linked list

    Methods:
      __str__(): returns a string representation of the value of the node
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    """
    Instantiates a singly linked list.

    Attributes:
      head (node object, default = None): the head node in the linked list

    Methods:
      __str__(): returns a string representation of the values of the nodes in the linked list
      insert(value): no return, creates a new node at the head of the linked list and assigns the value attribute
      includes(value): returns True or False if the input value exactly matches a node value in the linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list_string = ''
        current_node = self.head
        while current_node:
            current_node_string = current_node.__str__()
            linked_list_string += f"{{ {current_node_string} }} -> "
            current_node = current_node.next
        linked_list_string += 'NULL'
        return linked_list_string

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        current_node = self.head

        if current_node is not None:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

class TargetError:
    pass
