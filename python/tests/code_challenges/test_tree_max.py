import pytest
from data_structures.binary_tree import BinaryTree, Node
from data_structures.invalid_operation_error import InvalidOperationError


# @pytest.mark.skip("TODO")
def test_max_val_left_max():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_max_val_right_max():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(60)

    actual = tree.find_maximum_value()
    expected = 60

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_max_val_root_max():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.left = Node(30)
    tree.root.right = Node(60)

    actual = tree.find_maximum_value()
    expected = 100

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_max_val_more_nodes():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(200)
    tree.root.left.right = Node(199)
    tree.root.right = Node(12)
    tree.root.right.right = Node(-25)

    actual = tree.find_maximum_value()
    expected = 200

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_max_val_empty():
    tree = BinaryTree()
    with pytest.raises(InvalidOperationError):
        tree.find_maximum_value()
