"""
Test for Stack
"""
import pytest
from my_stack import Stack



@pytest.fixture(name="stack")
def fixture_stack():
    """
    Fixture for an empty stack
    :return: Stack
    """
    return Stack()


@pytest.fixture(name="stack_val")
def fixture_stack_val():
    """
    Fixture for an stack with one node
    :return: Stack
    """
    return Stack('first')


@pytest.fixture(name="stack_big")
def fixture_stack_big():
    """
    Fixture for an stack with 6 nodes
    :return: Stack
    """
    my_stack = Stack("First node")
    my_stack.push("Second node")
    my_stack.push("Third node")
    my_stack.push("Fourth node")
    my_stack.push("Fifth node")
    my_stack.push("Sixth node")
    return my_stack


def test_stack_init_empty(stack):
    """
    Checks the stack was created empty
    """
    assert stack.peek is None
    assert len(stack) == 0


def test_stack_init_with_value(stack_val):
    """
    Checks the stack was created with one node
    """
    assert len(stack_val) == 1
    assert stack_val.peek == 'first'


def test_stack_push_into_empty_list(stack):
    """
    Checks that node pushs into the empty stack
    """
    stack.push('new value')
    assert stack.peek == 'new value'
    assert len(stack) == 1


def test_stack_push_into_stack_with_values(stack_val):
    """
    Checks that node pushes into the stack with one node
    """
    stack_val.push('second')
    assert stack_val.peek == 'second'
    assert len(stack_val) == 2


def test_stack_pop_from_empty_stack(stack):
    """
    Checks that node doesn't pops from empty stack
    """
    assert stack.pop() is None
    assert len(stack) == 0


def test_stack_pop_from_stack_with_one_node(stack_val):
    """
    Checks that node pops from stack with one node
    """
    assert stack_val.pop() == 'first'
    assert stack_val.peek is None
    assert len(stack_val) == 0


def test_stack_pop_from_stack_with_6_nodes(stack_big):
    """
    Checks that node pops from stack with 6 nodes
    """
    assert stack_big.pop() == 'Sixth node'
    assert stack_big.peek == 'Fifth node'
    assert len(stack_big) == 5
