"""
Test for Queue
"""
import pytest
from my_queue import MyQueue


@pytest.fixture(name="queue")
def fixture_queue():
    """
    Fixture for an empty queue
    :return: Queue
    """
    return MyQueue()


@pytest.fixture(name="queue_val")
def fixture_queue_val():
    """
    Fixture for an queue with one node
    :return: Queue
    """
    return MyQueue('first')


@pytest.fixture(name="queue_big")
def fixture_queue_big():
    """
    Fixture for an queue with 6 nodes
    :return: Queue
    """
    my_queue = MyQueue("First node")
    my_queue.enqueue("Second node")
    my_queue.enqueue("Third node")
    my_queue.enqueue("Fourth node")
    my_queue.enqueue("Fifth node")
    my_queue.enqueue("Sixth node")
    return my_queue


def test_queue_init_empty(queue):
    """
    Checks the queue was created empty
    """
    assert queue.peek is None
    assert len(queue) == 0


def test_queue_init_with_value(queue_val):
    """
    Checks the queue was created with one node
    """
    assert len(queue_val) == 1
    assert queue_val.peek == 'first'


def test_queue_enqueue_into_empty_queue(queue):
    """
    Checks that node enqueues into the end of empty queue
    """
    queue.enqueue('new value')
    assert queue.peek == 'new value'
    assert len(queue) == 1


def test_queue_enqueue_into_queue_with_values(queue_val):
    """
    Checks that node enqueues into the end of queue with one node
    """
    queue_val.enqueue('second')
    assert queue_val.peek == 'first'
    assert len(queue_val) == 2


def test_queue_dequeue_from_empty_queue(queue):
    """
    Checks that node doesn't dequeue from empty queue
    """
    assert queue.dequeue() is None
    assert len(queue) == 0


def test_queue_dequeue_from_queue_with_one_node(queue_val):
    """
    Checks that node dequeues from queue from queue with one node
    """
    assert queue_val.dequeue() == 'first'
    assert queue_val.peek is None
    assert len(queue_val) == 0


def test_queue_dequeue_from_queue_with_6_nodes(queue_big):
    """
    Checks that node dequeues from queue from queue with 6 nodes
    """
    assert queue_big.dequeue() == 'First node'
    assert queue_big.peek == 'Second node'
    assert len(queue_big) == 5
