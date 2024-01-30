from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Instantiates a binary search tree data structure. Extends the binary tree class.

    Methods:
        add(value): Adds a new node to the binary search tree at the appropriate location based on the given value. Values less than the root value are added as a child to the left and values greater than the root value are added as a child to the right. No return.
        contains(target_value): Returns a boolean of true or false indicating if a value if present in the binary search tree.
    """

    def add(self, value):
        """
        Adds a new node to the binary search tree at the appropriate location based on the given value. Values less than the root value are added as a child to the left and values greater than the root value are added as a child to the right. No return.

        Parameters:
            value (number): the numeric value of the node
        """

        new_node = Node(value)

        # if tree is empty then new node is root
        if self.root is None:
            self.root = new_node
            return

        # otherwise find the correct spot to add the new node at
        def bst_traverse_add(root_node, new_node):
            """
            Recursive function which traverses the binary search tree and adds a new node at the appropriate location based on its value. No return.

            Parameters:
                root_node (node object): root of tree or sub-tree to evaluate for suitability to add a new node as a child
                new_node (node object): a new node being added to the tree
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
        Returns a boolean of true or false indicating if a value if present in the binary search tree.

        Parameters:
            target_value (number): value to be searched for in the tree
        """

        def bst_traverse_contains(root_node, target_value):
            """
            Recursive function which traverses the binary search tree and evaluates if a given value is present in the tree. Returns a boolean indicating the presence of the value.

            Parameters:
                root_node (node object): root of tree or sub-tree to traverse for the target value
                target_value (number): value to compare and match against the tree's values
            """

            # tree is empty or no node contains target value
            if root_node is None:
                return False

            # node matches target value
            if root_node.value == target_value:
                return True

            # recursively call if target value < node value
            if target_value < root_node.value:
                return bst_traverse_contains(root_node.left, target_value)

            # recursively call if target value > node value
            if target_value > root_node.value:
                return bst_traverse_contains(root_node.right, target_value)

        return bst_traverse_contains(self.root, target_value)
