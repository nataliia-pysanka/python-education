"""
Tests for binary search algorithm
"""
import pytest
from binary_search import binary_search


@pytest.mark.parametrize("lst, item, index", [
    ([x**3 // 240 for x in range(100, 1100)], 4166, 0),
    ([x**3 // 240 for x in range(100, 1100)], 33333, 100),
    ([x**3 // 240 for x in range(100, 1100)], 112500, 200),
    ([x**3 // 240 for x in range(100, 1100)], 266666, 300),
    ([x**3 // 240 for x in range(100, 1100)], 520833, 400),
    ([x**3 // 240 for x in range(100, 1100)], 900000, 500),
    ([x**3 // 240 for x in range(100, 1100)], 1429166, 600),
    ([x**3 // 240 for x in range(100, 1100)], 2133333, 700),
    ([x**3 // 240 for x in range(100, 1100)], 3037500, 800),
    ([x**3 // 240 for x in range(100, 1100)], 4166666, 900),
    ([x**3 // 240 for x in range(100, 1100)], 5530722, 999),
    ([x**3 // 240 for x in range(100, 1100)], 5555555, None),
    ([x**3 // 240 for x in range(100, 1100)], -5555555, None),
    ([x**3 // 240 for x in range(100, 1100)], 'd', None),
    ([], 1, None),
    (list('qwertyuiopasdfghjklzxcvbnm'), 'ee', None),
    ([1 for x in range(1000)], 1, 0)
])
def test_find_index(lst, item, index):
    """
    Check method with different values
    :param lst: list
    :param item: int
    :param index: int
    :return: int or None
    """
    assert binary_search(lst, item) == index
