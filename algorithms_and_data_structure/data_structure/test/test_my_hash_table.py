"""
Tests for hash-table
"""
import datetime
import pytest
from my_hash_table import MyHashTable

NUM = 100


def generate_item():
    """
    Generates unique sets of key and value
    :return:
    """
    key = str(datetime.datetime.now())
    item = f'this is item of {key}'
    return key, item


@pytest.fixture(name="table")
def fixture_table():
    """
    Fixture for an empty table
    :return: MyHashTable
    """
    return MyHashTable()


@pytest.fixture(name="table_val")
def fixture_table_val():
    """
    Fixture for the list with one node
    :return: MyHashTable
    """
    item = generate_item()
    my_table = MyHashTable()
    my_table.insert(item[0], item[1])
    return my_table


@pytest.fixture(name="dict_100")
def fixture_dict_100():
    """
    Fixture for the dict with keys
    :return: dict
    """
    dict_100 = {}
    for _ in range(NUM):
        item = generate_item()
        dict_100.update({item[0]: item[1]})
    return dict_100


@pytest.fixture(name="table_100")
def fixture_table_100():
    """
    Fixture for the table with 100 nodes
    :return: MyHashTable
    """
    my_table = MyHashTable()
    for _ in range(NUM):
        item = generate_item()
        my_table.insert(item[0], item[1])
    return my_table


def test_table_insert_to_empty(table):
    """
    Checks the value inserts to the empty table
    """
    item = generate_item()
    table.insert(item[0], item[1])
    assert table.lookup(item[0]) == item[1]
    assert len(table) == 1


def test_table_insert(table_val, dict_100):
    """
    Checks the value inserts to the table with items
    """
    print(len(dict_100))
    for key, value in dict_100.items():
        table_val.insert(key, value)
    assert len(table_val) == 1 + NUM
    for key, value in dict_100.items():
        assert table_val.lookup(key) == value


def test_table_lookup_of_empty(table):
    """
    Checks the value lookups in the empty table
    """
    assert table.lookup('key') is None
    assert len(table) == 0


def test_table_lookup(table_100, dict_100):
    """
    Checks the value lookups in the table with items
    """
    for key, value in dict_100.items():
        table_100.insert(key, value)
    assert len(table_100) == NUM * 2
    for key, value in dict_100.items():
        assert table_100.lookup(key) == value


def test_table_delete_from_empty(table):
    """
    Checks the value deletes in the empty table
    """
    assert table.delete('key') is None
    assert len(table) == 0


def test_table_delete(table_100, dict_100):
    """
    Checks the value lookups in the table with items
    """
    for key, value in dict_100.items():
        table_100.insert(key, value)
    assert len(table_100) == NUM * 2
    for key, value in dict_100.items():
        table_100.delete(key)
    assert len(table_100) == NUM
