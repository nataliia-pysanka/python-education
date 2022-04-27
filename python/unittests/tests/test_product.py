"""
Test module for Product class
"""
import pytest
from product import Product, InsufficientAmount


@pytest.fixture(name="product_normal")
def fixture_product_normal():
    """
    Returns a product instance with title='product', price=20.0, quantity=200
    """
    return Product('product', 20, 200)


@pytest.fixture(name="product_with_args")
def fixture_product_with_args():
    """
    Returns a product instance with title='product', price=20.0
    """
    return Product('product', 20.0)


def test_product_init_with_three_arg(product_normal):
    """
        Initializes object of Product class with three arguments
    """
    assert product_normal.quantity == 200


# def test_product_exception_with_no_arg():
#     """
#         Initializes object of Product class with no arguments
#     """
#     with pytest.raises(TypeError):
#         Product()


def test_product_init_exception_on_negative_quantity():
    """
        Initializes object of Product class with negative quantity
    """
    with pytest.raises(InsufficientAmount):
        Product('product', 20.0, -32)


def test_product_init_exception_on_incorrect_type_name():
    """
        Initializes object of Product class with incorrect type of first
        argument. Should be str
    """
    with pytest.raises(TypeError):
        Product(324, 20.0, 32)


def test_product_init_exception_on_incorrect_type_price():
    """
        Initializes object of Product class with incorrect type of second
        argument. Should be float (or int)
    """
    with pytest.raises(TypeError):
        Product('product', 'price', 32)


def test_product_init_exception_on_incorrect_type_quantity():
    """
        Initializes object of Product class with incorrect type of third
        argument. Should be int
    """
    with pytest.raises(TypeError):
        Product('product', 20, 32.0)


def test_product_init_with_args(product_with_args):
    """
        Initializes object of Product class with first and second arguments.
        Third argument should be by default
    """
    assert product_with_args.quantity == 1


def test_product_subtract_quantity(product_normal):
    """
        Initializes object of Product class with first and second arguments.
        Third argument should be by default
    """
    product_normal.subtract_quantity(10)
    assert product_normal.quantity == 190


def test_product_subtract_exception_on_insufficient_amount(product_with_args):
    """
        Subtracts more than amount
    """
    with pytest.raises(InsufficientAmount):
        product_with_args.subtract_quantity(10)


def test_product_add_quantity(product_normal):
    """
        Adds positive quantity
    """
    product_normal.add_quantity(10)
    assert product_normal.quantity == 210


def test_product_add_exception_on_negative_arg_under_zero(product_normal):
    """
        Adds negative quantity: sum will be under 0
    """
    with pytest.raises(InsufficientAmount):
        product_normal.add_quantity(-256)


def test_product_add_exception_on_negative_arg(product_normal):
    """
        Adds negative quantity: sum will be more then 0
    """
    product_normal.add_quantity(-156)
    assert product_normal.quantity == 44


def test_product_change_price_on_int(product_normal):
    """
        Changes price on integer number
    """
    product_normal.change_price(5)
    assert product_normal.price == 5.0


def test_product_change_price_on_float(product_normal):
    """
        Changes price on float number
    """
    product_normal.change_price(5.0)
    assert product_normal.price == 5.0


def test_product_change_price_on_str(product_normal):
    """
        Changes price on non float or integer number
    """
    with pytest.raises(TypeError):
        product_normal.change_price('5.0')


@pytest.mark.parametrize("increment, sold, expected", [
    (145, 65, 280),
    (0, 200, 0)
])
def test_transactions(product_normal, increment, sold, expected):
    """
        Checks transactions with different numbers
    """
    product_normal.add_quantity(increment)
    product_normal.subtract_quantity(sold)
    assert product_normal.quantity == expected
