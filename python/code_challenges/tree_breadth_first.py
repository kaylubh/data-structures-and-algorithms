from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(binary_tree):
    """
    Conducts a breadth-first traversal of a input binary tree and returns the ordered values of its nodes in a list.

    Parameters:
        binary_tree (binary tree object): binary tree with nodes that contain left and right attributes

    Returns:
        list: a list of the binary trees nodes values in breadth-first order
    """

    breadth_traversal = Queue()

    if binary_tree.root is not None:
        breadth_traversal.enqueue(binary_tree.root)

    breadth_first_ordered_nodes = []

    while breadth_traversal.is_empty() == False:

        current_node = breadth_traversal.dequeue()

        if current_node.left is not None:
            breadth_traversal.enqueue(current_node.left)

        if current_node.right is not None:
            breadth_traversal.enqueue(current_node.right)

        breadth_first_ordered_nodes.append(current_node.value)

    return breadth_first_ordered_nodes
