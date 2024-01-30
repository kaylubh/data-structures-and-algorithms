from data_structures.invalid_operation_error import InvalidOperationError

class BinaryTree:
    """
    Instantiates a binary tree data structure.

    Attributes:
        root (node object, default = None): root node of the tree

    Class Methods:
        depth_traversal(root_node, order): Recursive function which conducts a depth traversal of the binary tree from a given root node and returns the values from the tree in the specified order.

    Instance Methods:
        pre_order(): Returns a list of the values of the binary tree with the pre-order method. root >> left >> right
        in_order(): Returns a list of the values of the binary tree with the in-order method. left >> root >> right
        post_order(): Returns a list of the values of the binary tree with the post-order method. left >> right >> root
        find_maximum_value(): Returns the maximum value in the binary tree. Assumes all values in the tree are numeric.
    """

    def __init__(self):
        self.root = None

    @classmethod
    def depth_traversal(cls, root_node, order):
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
        left_value = cls.depth_traversal(root_node.left, order)
        right_value = cls.depth_traversal(root_node.right, order)

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

        return self.depth_traversal(self.root, "pre")

    def in_order(self):
        """
        Returns a list of the values of the binary tree with the in-order method. left >> root >> right
        """

        return self.depth_traversal(self.root, "in")

    def post_order(self):
        """
        Returns a list of the values of the binary tree with the post-order method. left >> right >> root
        """

        return self.depth_traversal(self.root, "post")

    def find_maximum_value(self):
        """
        Returns the maximum value in the binary tree. Assumes all values in the tree are numeric.
        """

        if self.root is None:
            raise InvalidOperationError("Method not allowed on empty tree")

        def max_traversal(root_node, max_value):
            """
            Recursive function which traverses all nodes in a binary tree from a given root and evaluates their values in order to return the maximum value in the tree. Assumes all nodes have numeric values.

            Parameters:
                root_node (node object): node to begin the traversal from
                max_value (number): current maximum value determined preceding each function call

            Returns:
                number: maximum value in the tree
            """

            if root_node.value > max_value:
                max_value = root_node.value

            if root_node.left is not None:
                max_value = max_traversal(root_node.left, max_value)

            if root_node.right is not None:
                max_value = max_traversal(root_node.right, max_value)

            return max_value

        return max_traversal(self.root, self.root.value)

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
