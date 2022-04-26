"""
Tests for even_odd() function
"""
import pytest
from functions import even_odd


def test_even_odd_raises_exception_on_non_integer_arguments():
    """
        Inputs to the method non integer number
    """
    with pytest.raises(TypeError):
        even_odd('test')


def test_even_odd_even_of_positive():
    """
        Inputs to the method even integer number
    """
    assert even_odd(4) == "even"


def test_even_odd_odd_of_positive():
    """
        Inputs to the method odd integer number
    """
    assert even_odd(3) == "odd"


def test_even_odd_even_of_negative():
    """
        Inputs to the method negative even integer number
    """
    assert even_odd(-4) == "even"


def test_even_odd_odd_of_negative():
    """
        Inputs to the method negative odd integer number
    """
    assert even_odd(-3) == "odd"
