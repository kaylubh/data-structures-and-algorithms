from data_structures.stack import Stack

class PseudoQueue:
    """
    Instantiates a queue data structure implemented using two stack data structures. Requires the Node class.
    """

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        """
        Enqueues (adds) a new node to the back of the queue. The top of stack_a is the back of the queue. No return.

        Parameters:
        value (any): the value to be assigned to the nodes value attribute
        """

        self.stack_a.push(value)

    def dequeue(self):
        """
        Dequeues (removes) the node at the front of the queue. Moves all nodes from stack_a to stack_b, the top of stack_b is the front of the queue. After dequeueing, moves all nodes back to stack_a for future operations. Returns the dequeued node.
        """

        # move nodes from stack_a to stack_b, top of stack_b is the back of the queue
        while self.stack_a.top is not None:
            node_to_move = self.stack_a.pop()
            self.stack_b.push(node_to_move)

        # store top of stack_b (the back of the queue) to be returned
        output = self.stack_b.pop()

        # return nodes to stack_a
        while self.stack_b.top is not None:
            node_to_move = self.stack_b.pop()
            self.stack_a.push(node_to_move)

        return output
