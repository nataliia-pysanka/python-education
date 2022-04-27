"""
Tests for BinarySearchTree
"""
import pytest
from binary_search_tree import BinarySearchTree, Node


@pytest.fixture(name="tree")
def fixture_tree():
    """
    Fixture for an empty tree
    :return: BinarySearchTree
    """
    return BinarySearchTree()


@pytest.fixture(name="tree_val")
def fixture_tree_val():
    """
    Fixture for an tree with one node
    :return: BinarySearchTree
    """
    return BinarySearchTree(0)


@pytest.fixture(name="tree_big")
def fixture_tree_big():
    """
    Fixture for an tree with 7 nodes
    :return: BinarySearchTree
    """
    tree = BinarySearchTree(100)
    tree.insert(125)
    tree.insert(99)
    tree.insert(455)
    tree.insert(2)
    tree.insert(1)
    tree.insert(67)
    return tree


def test_tree_init_empty(tree):
    """
    Checks the tree was created empty
    """
    assert tree.head is None
    assert len(tree) == 0


def test_tree_init_with_value(tree_val):
    """
    Checks the tree was created with one node
    """
    assert isinstance(tree_val.head, Node)
    assert len(tree_val) == 1
    assert tree_val.head.value == 0
    assert tree_val.head.left is None
    assert tree_val.head.right is None


def test_tree_insert_into_empty_tree(tree):
    """
    Checks that node inserts into the head of the empty tree
    """
    tree.insert(125)
    assert tree.head.value == 125
    assert len(tree) == 1


def test_tree_raise_with_not_number_value(tree):
    """
    Checks raising TypeError on not number value
    """
    with pytest.raises(TypeError):
        tree.insert('125')


def test_tree_lookup_in_empty_tree(tree):
    """
    Checks that node lookups in the empty tree
    """
    assert tree.lookup(125) is None
    assert len(tree) == 0


def test_tree_delete_from_empty_tree(tree):
    """
    Checks that node not deletes from the empty tree
    """
    assert tree.delete(125) is None
    assert len(tree) == 0


@pytest.mark.parametrize("insert, expected", [
    (280, True),
    (0, True),
    (100, None),
    (-5.0, True)
])
def test_inserts(tree_big, insert, expected):
    """
        Checks transactions with different numbers
    """
    assert tree_big.insert(insert) == expected


@pytest.mark.parametrize("delete, expected", [
    (280, None),
    (2, True),
    (100, True),
    (-5.0, None)
])
def test_deletes(tree_big, delete, expected):
    """
        Checks transactions with different numbers
    """
    assert tree_big.delete(delete) == expected
