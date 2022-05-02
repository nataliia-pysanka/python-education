"""
Tests for recursive factorial implementation
"""
import pytest
from factorial import factorial


@pytest.mark.parametrize("input_item, output_item", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
    (13, 6227020800),
    (14, 87178291200),
    (15, 1307674368000),
    (16, 20922789888000),
    (17, 355687428096000),
    (18, 6402373705728000),
    (19, 121645100408832000),
    (20, 2432902008176640000),
    (25, 15511210043330985984000000)
])
def test_factorial(input_item, output_item):
    """
    Checks method with different values
    :param input_item: int
    :param output_item: int
    """
    assert factorial(input_item) == output_item


def test_raise_value_error():
    """
    Checks the method raises ValueError if inputted number is negative
    """
    with pytest.raises(ValueError):
        factorial(-6)
