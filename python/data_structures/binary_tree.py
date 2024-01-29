class BinaryTree:
    """
    Instantiates a binary tree data structure.

    Attributes:
        root (node object, default = None): root node of the tree

    Class Methods:
        traverse(root_node, order):

    Instance Methods:
        pre_order():
        in_order():
        post_order():
    """

    def __init__(self):
        self.root = None

    @classmethod
    def traverse(cls, root_node, order):
        """
        Recursive function which conducts a depth traversal of the binary tree from a given root node and returns the values from the tree in the specified order.

        Parameters:
            root_node (node object): node to begin the traversal from
            order (string): depth traversal ordering, must be "pre", "in", or "post"

        Returns:
            list: values of the tree in the specified order
        """

        if root_node is None:
            return []

        root_value = [root_node.value]
        left_value = cls.traverse(root_node.left, order)
        right_value = cls.traverse(root_node.right, order)

        if order == "pre":
            return root_value + left_value + right_value

        if order == "in":
            return left_value + root_value + right_value

        if order == "post":
            return left_value + right_value + root_value

    def pre_order(self):
        """
        Returns a list of the values of the binary tree with the pre-order method. root >> left >> right
        """

        return self.traverse(self.root, "pre")

    def in_order(self):
        """
        Returns a list of the values of the binary tree with the in-order method. left >> root >> right
        """

        return self.traverse(self.root, "in")

    def post_order(self):
        """
        Returns a list of the values of the binary tree with the post-order method. left >> right >> root
        """

        return self.traverse(self.root, "post")

class Node:
    """
    Instantiates a node with the input value.

    Attributes:
      value (any): value or data stored in node
      left (node object, default = None): child node to the left in a tree
      right (node object, default = None): child node to the right in a tree
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
