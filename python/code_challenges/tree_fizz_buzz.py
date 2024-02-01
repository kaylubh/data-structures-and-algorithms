from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(kary_tree):
    """
    Applies the FizzBuzz algorithm to a given k-ary tree.

    Args:
        kary_tree (KaryTree): The k-ary tree to apply the FizzBuzz algorithm to.

    Returns:
        KaryTree: A new k-ary tree with the values converted according to the FizzBuzz algorithm.
    """

    def fizz_buzz_node_converter(node):
        """
        Converts the value of a node in a tree to "Fizz", "Buzz", "FizzBuzz", or a string representation of the value according to the rules of the FizzBuzz algorithm.

        Args:
            node: The node to convert.

        Returns:
            None
        """

        if node is None:
            return

        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            fizz_buzz_node_converter(child)

    fizzy_buzzy_tree = kary_tree.clone()

    fizz_buzz_node_converter(fizzy_buzzy_tree.root)

    return fizzy_buzzy_tree
