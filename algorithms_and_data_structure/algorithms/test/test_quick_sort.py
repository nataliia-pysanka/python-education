"""
Tests for quick sort algorithm
"""
import random
from quick_sort import quick_sort


def test_quick_sort():
    """
    Tests sorting with different lists
    :return:
    """
    for _ in range(101):
        lst = [int(random.random() * 100) for x in range(1000)]
        assert quick_sort(lst) == sorted(lst)
