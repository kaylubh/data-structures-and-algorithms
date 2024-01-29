from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        """

        """

        new_node = Node(value)

        # if tree is empty then new node is root
        if self.root is None:
            self.root = new_node
            return

        # otherwise find the correct spot to add the new node at
        def bst_traverse_add(root_node, new_node):
            """

            """

            if new_node.value < root_node.value:

                if root_node.left is None:
                    root_node.left = new_node
                else:
                    bst_traverse_add(root_node.left, new_node)

            elif new_node.value >= root_node.value:

                if root_node.right is None:
                    root_node.right = new_node
                else:
                    bst_traverse_add(root_node.right, new_node)

        bst_traverse_add(self.root, new_node)

    def contains(self, target_value):
        """

        """

        node_to_check = self.root

        while node_to_check is not None:
            if target_value < node_to_check.value:
                node_to_check = node_to_check.left
            elif target_value > node_to_check.value:
                node_to_check = node_to_check.right

        return node_to_check.value == target_value
