"""
Test module for Shop class
"""
import pytest
from product import Product
from shop import Shop


@pytest.fixture(name='shop')
def fixture_shop():
    """
    Returns an empty shop instance
    """
    return Shop()


@pytest.fixture(name='product_1')
def fixture_product_1():
    """
    Returns a product instance with title='product_1', price=20.0, quantity=200
    """
    return Product('product_1', 20, 200)


@pytest.fixture(name='product_2')
def fixture_product_2():
    """
    Returns a product instance with title='product_2', price=34.0, quantity=120
    """
    return Product('product_2', 32, 120)


@pytest.fixture(name='big_shop')
def fixture_big_shop(product_1):
    """
    Returns a shop with products
    """
    return Shop(product_1)


def test_shop_init_with_no_args(shop):
    """
        Initializes object of Shop class with no arguments
    """
    assert shop.products == []


def test_shop_init_with_product(big_shop, product_1):
    """
        Initializes object of Shop class with argument product_1
    """
    assert big_shop.products == [product_1]


def test_shop_add_product(big_shop, product_1):
    """
        Adds product to the shop
    """
    big_shop.add_product(product_1)
    assert big_shop.products == [product_1, product_1]


def test_shop_add_product_with_no_args(big_shop):
    """
        Calls method add_product with no product in arguments
    """
    with pytest.raises(TypeError):
        big_shop.add_product()


def test_shop_add_product_with_other_type_product(big_shop, product_1):
    """
        Adds product with no Product type to the shop
    """
    big_shop.add_product('product')
    assert big_shop.products == [product_1, 'product']


# def test_shop_get_product_index(big_shop, product_1):
#     """
#         Gets product item from the shop
#     """
#     assert big_shop._get_product_index(product_1.title) == 0


# def test_shop_get_product_index_with_wrong_title(big_shop):
#     """
#         Calls method for _get_product_index with wrong title
#     """
#     assert big_shop._get_product_index('title') is None


def test_shop_get_product_index_with_wrong_title(big_shop):
    """
        Calls method for _get_product_index with wrong title
    """
    assert big_shop.sell_product('title') is None


def test_shop_sell_product(big_shop):
    """
        Sells product from the shop and get receipt
    """
    assert big_shop.sell_product('product_1', 1) == 20.0


def test_shop_sell_product_exception_on_big_quantity(big_shop):
    """
        Tries to sell more products then quantity
    """
    with pytest.raises(ValueError):
        big_shop.sell_product('product_1', 300)


def test_shop_sell_product_check_money(big_shop):
    """
        Cells product and checks money in the shop
    """
    big_shop.sell_product('product_1', 50)
    assert big_shop.money == 1000.0


def test_shop_sell_product_check_availability_after(big_shop, product_1):
    """
        Cells products and check availability in the shop
    """
    big_shop.sell_product('product_1', 50)
    assert big_shop.products == [product_1]


def test_shop_sell_product_all_check_availability_after(big_shop):
    """
        Cells all of products quantity and check availability in the shop
    """
    big_shop.sell_product('product_1', 200)
    assert big_shop.products == []
