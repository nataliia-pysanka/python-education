from product import Product, InsufficientAmount


class Shop:
    """Representation of the shop

    Args:
        products (list or Product, optional): products to add to a shop while creating it.
    """

    def __init__(self, products=None):
        if products is None:
            products = []
        elif isinstance(products, Product):
            products = [products]
        self.products = products
        self.money = .0

    def add_product(self, product):
        """Adds product to the shop.

        Args:
            product (Product): product to add to the shop.
        """
        self.products.append(product)

    def _get_product_index(self, product_title):
        """Looks for products in the shop.

        Args:
            product_title (str): title of the product to look for.

        Returns:
            int: the index of the product if it present in the shop else None
        """
        for index, product in enumerate(self.products):
            if product.title == product_title:
                return index
        return None

    def sell_product(self, product_title, qty_to_sell=1):
        """Sells product and returns the final money amount to pay.

        Args:
            product_title (str): the title of the product to sell.
            qty_to_sell (int, optional): the quantity of the product to sell.
                Defaults to 1.

        Raises:
            ValueError: in case if amount of available products
                of that type is less then given.

        Returns:
            float: money amount to pay.
        """
        product_index = self._get_product_index(product_title)
        receipt = .0
        if product_index is not None:
            if self.products[product_index].quantity < qty_to_sell:
                raise ValueError('Not enough products')
            else:
                receipt = self.products[product_index].price * qty_to_sell
                if self.products[product_index].quantity == qty_to_sell:
                    del self.products[product_index]
                else:
                    self.products[product_index].subtract_quantity(qty_to_sell)
                self.money += receipt
            return receipt
