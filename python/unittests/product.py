class InsufficientAmount(Exception):
    pass


class Product:
    """Data class representation of a product in a shop.

    Args:
        title (str): title of the product
        price (float): price of one product
        quantity (int, optional): the amount of the product available.
            Defaults to 1
    """

    def __init__(self, title, price, quantity=1):
        if not isinstance(title, str):
            raise TypeError(
                "Title should be string"
            )
        self.title = title

        if price < 0:
            raise InsufficientAmount(
                "Quantity should be positive"
            )

        if isinstance(price, float) or isinstance(price, int):
            self.price = float(price)
        else:
            raise TypeError(
                "Price should be float or int"
            )

        if quantity < 0:
            raise InsufficientAmount(
                "Quantity should be positive"
            )
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise TypeError(
                "Quantity should be integer"
            )

    def subtract_quantity(self, num_of_products=1):
        """Subtracts the number of available products.

        Args:
            num_of_products (int, optional): number of products
                available to subtract. Defaults to 1.
        """
        if self.quantity < num_of_products:
            raise InsufficientAmount(
                f'Not enough available product to subtract {num_of_products}')
        self.quantity -= num_of_products

    def add_quantity(self, num_of_products=1):
        """Adds the number of available products.

        Args:
            num_of_products (int, optional): number of products
                available to add. Defaults to 1.
        """
        if self.quantity + num_of_products < 1:
            raise InsufficientAmount(
                f'Not enough available product to add {num_of_products}')
        self.quantity += num_of_products

    def change_price(self, new_price):
        """Changes price of one product.

        Args:
            new_price (float): the price to change to.
        """
        if isinstance(new_price, float) or isinstance(new_price, int):
            self.price = float(new_price)
        else:
            raise TypeError(
                "New price should be float or int"
            )
