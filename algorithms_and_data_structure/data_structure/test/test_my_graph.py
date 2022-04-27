"""
Tests for graph
"""
import pytest
from my_graph import MyGraph
from my_linked_list import Node


@pytest.fixture(name="graph")
def fixture_graph():
    """
    Fixture for an empty graph
    :return: MyGraph
    """
    return MyGraph()


@pytest.fixture(name="graph_big")
def fixture_graph_big():
    """
    Fixture for an graph with 8 nodes
    :return: BinarySearchTree
    """
    graph = MyGraph()
    graph.insert('A', 'B', 'C', 'K')
    graph.insert('B', 'A', 'D', 'E', 'F')
    graph.insert('C', 'A')
    graph.insert('D', 'B')
    graph.insert('E', 'B', 'A')
    graph.insert('F', 'B', 'C', 'K')
    graph.insert('K', 'A')
    graph.insert('L', 'K')
    return graph


def test_graph_empty(graph):
    """
    Checks the tree was created empty
    """
    assert len(graph) == 0


def test_graph_init_with_value(graph_big):
    """
    Checks the graph was created with one node
    """
    assert len(graph_big) == 8


def test_graph_insert_into_empty_graph(graph):
    """
    Checks that node inserts into the empty graph
    """
    assert graph.insert('A') is True
    assert len(graph) == 1


def test_graph_insert_into_graph_with_items(graph_big):
    """
    Checks that node inserts into the graph with values
    """
    assert graph_big.insert('A') is None
    assert len(graph_big) == 8
    assert graph_big.insert('O') is True
    assert len(graph_big) == 9


def test_graph_lookups_in_graph_with_items(graph_big):
    """
    Checks that node lookups in the graph with values
    """
    assert isinstance(graph_big.lookup('A'), Node)
    assert graph_big.lookup('O') is None


def test_graph_delete_from_graph_with_items(graph_big):
    """
    Checks that node deletes from the graph with values
    """
    assert graph_big.delete('A') is True
    assert len(graph_big) == 7
    assert graph_big.delete('O') is None
    assert len(graph_big) == 7


def test_graph_delete_from_empty_graph(graph):
    """
    Checks that node deletes from the empty graph
    """
    assert graph.delete('A') is None
    assert len(graph) == 0
