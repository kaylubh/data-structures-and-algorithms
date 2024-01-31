from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node

class Queue:
    """
    Instantiates a queue data structure. Requires the Node class.
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Enqueues (adds) a new node to the back of the queue. No return.

        Parameters:
        value (any): the value to be assigned to the nodes value attribute
        """

        new_node = Node(value)

        # if queue is empty
        if self.back is None:
            self.back = new_node
            self.front = new_node

        # otherwise
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Dequeues (removes) the node at the front of the queue. Returns the dequeued node value.
        """

        # exceptions
        if self.front is None: # queue is empty
            raise InvalidOperationError("Method not allowed on empty collection")

        # dequeue
        dequeued_node = self.front
        self.front = dequeued_node.next

        # if queue is now empty
        if self.front is None:
            self.back = None

        return dequeued_node.value

    def peek(self):
        """
        Returns the value attribute of the node at the front of the queue. Does not remove the node.
        """

        # exceptions
        if self.front is None: # queue is empty
            raise InvalidOperationError("Method not allowed on empty collection")

        # peek
        return self.front.value

    def is_empty(self):
        """
        Returns a boolean indicating whether the queue is empty.
        """

        return self.front == None
