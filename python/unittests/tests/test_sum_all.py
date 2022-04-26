"""
Tests sum_all() method
"""
import pytest
from functions import sum_all


def test_sum_all_raises_exception_on_non_int_no_float_arguments():
    """
        Inputs to the method non float or integer number
    """
    with pytest.raises(TypeError):
        sum_all('test')


def test_sum_all_int():
    """
        Inputs to the method three integer numbers
    """
    assert sum_all(4, 9, 10) == 23


def test_sum_all_float():
    """
        Inputs to the method three float numbers
    """
    assert sum_all(3.0, 7.3, 8.9) == 19.200000000000003


def test_sum_all_int_float():
    """
        Inputs to the method integer and float numbers
    """
    assert sum_all(3, 5.2, 8.8, 12) == 29.0


@pytest.mark.parametrize("inpt, expected", [
    ([3, 5.2, 8.8, 12, 3, 5.2, 8.8, 12], 58.0),
    ([-1, 3.4, 8.9 -11.3678, 165, -44.00003], 120.93216999999999),
    ([-11.0004, 34545, 23593495, -3464564], 20163464.9996)
])
def test_sum_all_parametrize(inpt, expected):
    """
        Checks transactions with different numbers
    """
    assert sum_all(*inpt) == expected
