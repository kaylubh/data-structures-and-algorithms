class Node:
    """
    Represents a node in a singly linked list. Intended to be used with the LinkedList class which will instantiate nodes.

    Attributes:
      value (any): value or data stored in node
      next (node object, default = None): next node in linked list

    Methods:
      __str__(): returns a string representation of value of node
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
      head (node object, default = None): the head node in linked list

    Methods:
      __str__(): returns a string representation of values of nodes in linked list
      insert(value): no return, creates new node at head of linked list and assigns value attribute
      append(value): no return, creates new node at tail of linked list and assigns value attribute
      insert_before(target_node, new_value): no return, creates new node before target_node of linked list and assigns value attribute
      insert_after(target_node, new_value): no return, creates new node after target_node of linked list and assigns value attribute
      includes(value): returns True or False if input value exactly matches a node value in linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list_string = ''
        current_node = self.head

        while current_node:
            current_node_string = str(current_node)
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

    def insert_before(self, target_node, new_value):
        new_node = Node(new_value)
        current_node = self.head

        # raise exception if linked list is empty
        if current_node is None:
            raise TargetError("The linked list does not contain any nodes")

        # if head is target node
        if current_node.value == target_node:
            new_node.next = current_node
            self.head = new_node
            return

        # traverse linked list to find target node
        while current_node.next:
            if current_node.next.value == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

            else:
                current_node = current_node.next

        # raise exception if target not found
        raise TargetError("Target node not found in the linked list")

    def insert_after(self, target_node, new_value):
        new_node = Node(new_value)
        current_node = self.head

        # raise exception if linked list is empty
        if current_node is None:
            raise TargetError("The linked list does not contain any nodes")

        # traverse linked list to find target node
        while current_node:
            if current_node.value == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

            else:
                current_node = current_node.next

        # raise exception if target not found
        raise TargetError("Target node not found in the linked list")

    def includes(self, target_value):
        current_node = self.head

        while current_node:
            if current_node.value == target_value:
                return True
            current_node = current_node.next

        return False

class TargetError(Exception):
    pass
