from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node

class Stack:
    """
    Instantiates a stack data structure. Requires the Node class.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Pushes (adds) a new node to the top of the stack. No return.

        Parameters:
        value (any): the value to be assigned to the nodes value attribute
        """

        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pops (removes) the node at the top of the stack. Returns the popped node.
        """

        # exceptions
        if self.top is None: # stack is empty
            raise InvalidOperationError("Method not allowed on empty collection")

        # pop
        popped_node = self.top
        self.top = popped_node.next

        return popped_node.value

    def peek(self):
        """
        Returns the value attribute of the node at the top of the stack. Does not remove the node.
        """

        # exceptions
        if self.top is None: # stack is empty
            raise InvalidOperationError("Method not allowed on empty collection")

        # peek
        return self.top.value

    def is_empty(self):
        """
        Returns a boolean indicating whether the stack is empty. True for not empty and False for empty.
        """

        return self.top == None
