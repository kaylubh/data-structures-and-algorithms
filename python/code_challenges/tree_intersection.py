from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    """
    Find the values that are present in both tree_a and tree_b.

    Args:
        tree_a: The first binary tree.
        tree_b: The second binary tree.

    Returns:
        A list of values that are present in both tree_a and tree_b.
    """

    tree_a_values = tree_a.pre_order()
    tree_b_values = tree_b.pre_order()

    tree_a_map = Hashtable()
    for value in tree_a_values:
        if not tree_a_map.has(str(value)):
            tree_a_map.set(str(value), value)

    shared_values = Hashtable()
    for value in tree_b_values:
        if tree_a_map.has(str(value)):
            shared_values.set(str(value), value)

    return shared_values.values()
