"""
Test for linked list
"""
import pytest
from my_linked_list import LinkedList, Node


@pytest.fixture(name="lst")
def fixture_lst():
    """
    Fixture for an empty list
    :return: LinkedList
    """
    return LinkedList()


@pytest.fixture(name="lst_val")
def fixture_lst_val():
    """
    Fixture for an list with one node
    :return: LinkedList
    """
    return LinkedList('value')


@pytest.fixture(name="lst_big")
def fixture_lst_big():
    """
    Fixture for an list with 6 nodes
    :return: LinkedList
    """
    my_list = LinkedList("First node")
    my_list.append("Second node")
    my_list.append("Third node")
    my_list.append("Fourth node")
    my_list.append("Fifth node")
    my_list.append("Sixth node")
    return my_list


def test_linked_list_init_empty(lst):
    """
    Checks the list was created empty
    """
    assert lst.head is None
    assert len(lst) == 0


def test_linked_list_init_with_value(lst_val):
    """
    Checks the list was created with one node
    """
    assert isinstance(lst_val.head, Node)
    assert len(lst_val) == 1
    assert lst_val.head_value == 'value'
    assert lst_val.tail_value == 'value'


def test_linked_list_prepend_into_empty_list(lst):
    """
    Checks that node prepends into the head of the empty list
    """
    lst.prepend('new value')
    assert lst.head_value == 'new value'
    assert lst.tail_value == 'new value'
    assert len(lst) == 1


def test_linked_list_prepend_into_list_with_values(lst_val):
    """
    Checks that node prepends into the head of the list with value
    """
    lst_val.prepend('new value')
    assert lst_val.head_value == 'new value'
    assert lst_val.tail_value == 'value'
    assert len(lst_val) == 2


def test_linked_list_append_into_empty_list(lst):
    """
    Checks that node prepends into the head of the empty list
    """
    lst.append('new value')
    assert lst.head_value == 'new value'
    assert lst.tail_value == 'new value'
    assert len(lst) == 1


def test_linked_list_append_into_list_with_values(lst_val):
    """
    Checks that node prepends into the head of the list with value
    """
    lst_val.append('new value')
    assert lst_val.head_value == 'value'
    assert lst_val.tail_value == 'new value'
    assert len(lst_val) == 2


def test_linked_list_lookup(lst_big):
    """
    Checks the find of the first index of the existed value
    """
    assert lst_big.lookup("Fifth node") == 4


def test_linked_list_lookup_with_no_item(lst_big):
    """
    Checks the find of the first index of the value which doesn't exist
    """
    assert lst_big.lookup("Zero node") is None


def test_linked_list_insert_element_in_empty_list_on_0_index(lst):
    """
    Checks the insert node to the 0 index of empty list
    """
    lst.insert(0, 'new value')
    assert lst.head_value == 'new value'
    assert lst.tail_value == 'new value'
    assert len(lst) == 1


def test_linked_list_insert_element_in_empty_list_on_5_index(lst):
    """
    Checks the insert node to the 5 index of empty list
    """
    lst.insert(5, 'new value')
    assert lst.head_value == 'new value'
    assert lst.tail_value == 'new value'
    assert len(lst) == 1


def test_linked_list_insert_element_in_list_on_0_index(lst_big):
    """
    Checks the insert node to the 5 index of list with values
    """
    lst_big.insert(0, 'Zero node')
    assert lst_big.head_value == 'Zero node'
    assert lst_big.tail_value == 'Sixth node'
    assert len(lst_big) == 7


def test_linked_list_insert_element_in_list_on_the_last_index(lst_big):
    """
    Checks the insert node to the last index of list with values
    """
    length = len(lst_big)
    lst_big.insert(length-1, 'not last node')
    assert lst_big.head_value == 'First node'
    assert lst_big.tail_value == 'Sixth node'
    assert len(lst_big) == 7


def test_linked_list_delete_from_empty_list(lst):
    """
    Checks the deleting node from empty list
    """
    assert lst.delete(55) is None


def test_linked_list_delete_index_from_list_bigger_than_length(lst_big):
    """
    Checks the deleting node with index bigger than length of the list
    """
    assert lst_big.delete(55) is None


def test_linked_list_delete_index_from_head(lst_big):
    """
    Checks the deleting node from the head of the list
    """
    lst_big.delete(0)
    assert lst_big.head_value == 'Second node'
    assert lst_big.tail_value == 'Sixth node'
    assert len(lst_big) == 5


def test_linked_list_delete_index_from_tail(lst_big):
    """
    Checks the deleting node from the tail of the list
    """
    lst_big.delete(len(lst_big) - 1)
    assert lst_big.head_value == 'First node'
    assert lst_big.tail_value == 'Fifth node'
    assert len(lst_big) == 5


def test_linked_list_get_item_by_index(lst_big):
    """
    Checks the getitem method
    """
    assert lst_big[0] == "First node"
    assert lst_big[len(lst_big)] is None
    assert lst_big[len(lst_big) - 1] == "Sixth node"
    lst_big.append("Once more")
    assert lst_big[len(lst_big) - 1] == "Once more"
    assert lst_big[0] == "First node"
    lst_big.prepend("Zero node")
    assert lst_big[len(lst_big) - 1] == "Once more"
    assert lst_big[0] == "Zero node"


def test_linked_list_with_one_element_get_item_by_index(lst_val):
    """
    Checks the getitem method for list with one item
    """
    assert lst_val[0] == "value"


def test_linked_list_with_no_element_get_item_by_index(lst):
    """
    Checks the getitem method for list with one item
    """
    assert lst[0] is None
