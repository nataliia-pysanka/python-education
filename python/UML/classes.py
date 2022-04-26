"""
Demo-lasses for restaurant
"""


class Order:
    """
    Order depicts the order associated with a particular waiter or customer
    """
    _id = 0

    def __init__(self, _id=None, customer_id=None, waiter_id=None,
                 restaurant_id=None):
        Order._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Order._id
        self.customer_id = customer_id
        self.waiter_id = waiter_id
        self.restaurant_id = restaurant_id
        self.dishes = {}

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def add_dish(self, dish, cost):
        """
        Add dish with cost to the current order
        :param dish: str
        :param cost: int
        :return:
        """
        if self.dishes.get(dish):
            self.dishes[dish] += cost
        else:
            self.dishes[dish] = cost

    def del_dish(self, dish, value):
        """
        Delete dish with cost to the current order
        :param dish: str
        :param value: int
        :return:
        """
        if self.dishes.get(dish, 0) > value:
            self.dishes[dish] -= value
        else:
            del self.dishes[dish]

    def show_order(self):
        """
        Prints order with items and costs
        :return:
        """
        print(f"Order {self._id}:")
        for key, value in self.dishes.items():
            print(f" - {key}: {value}")


class Person:
    """
    It contains the details of the Person. There are two kinds of persons:
    the employee and the customer. This Person class is the parent class of
    two subclass –  Employee and Customer
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', adress='', phone=''):
        Person._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Person._id
        self.name = name
        self.adress = adress
        self.phone = phone
        self.birth = None

    def __str__(self):
        return f"Person {self.name}"

    def show_data(self):
        """
        Prints information about current person
        :return:
        """
        for key, value in self.__dict__.items():
            print(f"{key.capitalize()}: {value}")
        print()

    def change_data(self, key, value):
        """
        Change information about current person
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value


class Customer(Person):
    """
    It contains the details of the customer
    """
    def __init__(self, _id=None, name='', adress='', phone=''):
        Person.__init__(self, _id, name, adress, phone)
        self.orders = []
        self.discount = 0

    def create_order(self):
        """
        Create new order
        :return: obj
        """
        order = Order(self._id, waiter_id=None, restaurant_id=None)
        self.orders.append(order.get_id)
        return order

    def inc_order(self, order: Order, key, amount, value):
        """
        Add new item to the order
        :param order: Order
        :param key: str
        :param amount: int
        :param value: int
        :return:
        """
        if order.get_id in self.orders:
            for _ in range(amount):
                order.add_dish(key, value)

    def dec_order(self, order: Order, key, amount, value):
        """
        Decrement item in the order
        :param order: Order
        :param key: str
        :param amount: int
        :param value: int
        :return:
        """
        if order.get_id in self.orders:
            for _ in range(amount):
                order.del_dish(key, value)

    def cancel_order(self, order: Order):
        """
        Delete order
        :param order: Order
        :return:
        """
        self.orders.remove(order.get_id)


class Employee(Person):
    """
    It contains the details of the Employee. There are two kinds of employees,
    waiter and the chef. This employee class is the parent class of two
    subclass – Waiter and Chef
    """
    def __init__(self, _id=None, restaurant_id=None, name='', adress='',
                 phone=''):
        Person.__init__(self, _id, name, adress, phone)
        self.restaurant = restaurant_id
        self.position = None
        self.salary = None

    def change_position(self, position):
        """
        Changes the position
        :param position:
        :return:
        """
        self.position = position.name


class Waiter(Employee):
    """
    It contains the details of the  the order which is currently serving
    """
    def __init__(self, _id=None, name='', adress='', phone=''):
        Employee.__init__(self, _id, name, adress, phone)
        self.orders = []
        self.position = 'waiter'

    def take_order(self):
        """
        Create new order
        :return: Order
        """
        order = Order(customer_id=None, waiter_id=self._id, restaurant_id=None)
        self.orders.append(order.get_id)
        return order

    def inc_order(self, order: Order, key, amount, value):
        """
        Add new item to the order
        :param order: Order
        :param key: str
        :param amount: int
        :param value: int
        :return:
        """
        if order.get_id in self.orders:
            for _ in range(amount):
                order.add_dish(key, value)

    def dec_order(self, order: Order, key, amount, value):
        """
        Decrement item in the order
        :param order: Order
        :param key: str
        :param amount: int
        :param value: int
        :return:
        """
        if order.get_id in self.orders:
            for _ in range(amount):
                order.del_dish(key, value)

    def close_order(self, order: Order):
        """
        Close the order
        :param order:
        :return:
        """
        if order.get_id in self.orders:
            self.orders.remove(order.get_id)
        print(f"Order {order.get_id} is closed")


class Chef(Employee):
    """
    It contains the details of the chef working on a particular order
    """
    def __init__(self, _id=None, name='', adress='', phone=''):
        Employee.__init__(self, _id, name, adress, phone)
        self.orders = []
        self.position = 'chef'

    def take_order(self, order: Order):
        """
        Add an order to the current chef list
        :param order: Order
        :return:
        """
        self.orders.append(order.get_id)
        print("Chef is cooking..")
        return True

    def close_order(self, order: Order):
        """
        Delete an order from the current chef list
        :param order: Order
        :return:
        """
        if order.get_id in self.orders:
            self.orders.remove(order.get_id)
        print("The order is ready..")


class Position:
    """
    It contains all the responsibilities for each kind of employee
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', duties=''):
        Position._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Position._id
        self.name = name
        self.duties = duties

    def add_duty(self, duty: str):
        """
        Append the information to the list
        :param duty: str
        :return:
        """
        self.duties.append(duty)

    def delete_duty(self, duty: str):
        """
        Delete the information from the list
        :param duty: str
        :return:
        """
        try:
            self.duties.remove(duty)
        except ValueError:
            print(f"'{duty}' doesn't exist")

    def show_data(self):
        """
        Prints the information about current position
        :return:
        """
        print(f'Position "{self.name}" has the following responsibilities:')
        for duty in self.duties:
            print(f' - {duty}.')
        print()

    def change_data(self, key, value):
        """
        Changes the information for current position
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value


class Restaurant:
    """
    This class depicts the entire restaurant and says adress and contacts
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', adress='', opened=False):
        Restaurant._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Restaurant._id
        self.name = name
        self.adress = adress
        self.opened = opened

    def change_data(self, key, value):
        """
        Change the data about current restaurant
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value

    def open(self):
        """
        Opens or closes the restaurant
        :return:
        """
        self.opened = not self.opened

    def show_data(self):
        """
        Shows the information about current restaurant
        :return:
        """
        print(f'Restaurant "{self.name}" placed on {self.adress}.\n')


class Bill:
    """
    Bill is calculated using the order and menu.
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, *args):
        Bill._id += 1
        self.bill_id = Bill._id
        self.orders = args
        self._total = 0

    @property
    def total(self):
        """
        Returns total bill
        :return:
        """
        self.calculate_bill()
        return self._total

    def calculate_bill(self):
        """
        Calculates the bill from the orders
        :return: int
        """
        for order in self.orders:
            for value in order.dishes.values():
                self._total += value


class Payment:
    """
    This class is for doing payment. The payment can be done in two ways
    either cash or card. So payment is the parent class and cash and card are
    subclasses.
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __str__(self):
        return "Payment"

    def __init__(self, bill: Bill):
        Payment._id += 1
        self.payment_id = Payment._id
        self.bill_id = bill.get_id
        self.is_paid = False


class Card(Payment):
    """
    Payment can be done by  card or online
    """
    def __init__(self, bill: Bill):
        Payment.__init__(self, bill)

    def __str__(self):
        return 'Payment via card'

    def pay(self):
        """
        Makes pay via pay service
        :return:
        """
        print('You are going to the pay service..')
        print('...')
        print('Thank you')
        self.is_paid = True


class Cash(Payment):
    """
    Payment can be done by cash
    """
    def __init__(self, bill: Bill):
        Payment.__init__(self, bill)

    def __str__(self):
        return 'Payment with cash'

    def pay(self):
        """
        Makes pay via cash
        :return:
        """
        print("Please take the rest..")
        print('Thank you')
        self.is_paid = True


class Menu:
    """
    Menu contains all the food items available in the restaurant, their
    availability, price, etc.
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', date='', dishes=None):
        Menu._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Menu._id
        self.name = name
        self.date = date
        self.dishes = dishes

    def add_dish(self, key, value):
        """
        Adds new dish to the current menu
        :param key: str
        :param value: str
        :return:
        """
        self.dishes[key] = value

    def show_menu(self):
        """
        Prints the whole items in the current menu
        :return:
        """
        print('\t\t---------------------------')
        print(f"\t\tMenu '{self.name}':")
        print('\t\t---------------------------')
        for key, value in self.dishes.items():
            print(f"\t\t{key}: {value}")
        print('\t\t---------------------------')

    def change_data(self, key, value):
        """
        Changes the information in the current menu
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value


class Dish:
    """
    It contains all the food ingredients required for the dish item in menu
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', ingredients=dict, weight=0, cost=0):
        Dish._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Dish._id
        self.name = name
        self.ingredients = ingredients
        self.weight = weight
        self.cost = cost

    def remove_ingredient(self, ingredient):
        """
        Delete ingredient from the current dish
        :param ingredient: str
        :return:
        """
        if self.ingredients.get(ingredient):
            del self.ingredients[ingredient]

    def add_ingredient(self, ingredient, weight):
        """
        Add ingredient to the current dish
        :param ingredient:
        :param weight:
        :return:
        """
        self.ingredients.update({ingredient: weight})

    def show_dish(self):
        """
        Prints the information about current dish
        :return:
        """
        print(f"{self.name} costs {self.cost}")
        for key, value in self.ingredients.items():
            print(f" - {key}: {value}")
        print()

    def change_data(self, key, value):
        """
        Changes the information in the current dish
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value


class Product:
    """
    Product contains all details about product item in the restaurant storeroom
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, provider_id='', name='', count=''):
        Product._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Product._id
        self.provider_id = provider_id
        self.name = name
        self.count = count
        self.date_delivery = None
        self.date_expiration = None

    def show_product(self):
        """
        Prints the information about current product
        :return:
        """
        print(f"Product {self.name}: {self.count} units\n"
              f"Date of delivery: {self.date_delivery}\n"
              f"Date of expiration: {self.date_expiration}\n")

    def change_data(self, key, value):
        """
        Changes the information in the current product
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value


class Provider:
    """
    It contains all details about provider of products for current restaurant
    """
    _id = 0

    @property
    def get_id(self):
        """
        Getter for _id
        :return: str
        """
        return self._id

    def __init__(self, _id=None, name='', adress='', contacts=''):
        Provider._id += 1
        if _id:
            self._id = _id
        else:
            self._id = Provider._id
        self.name = name
        self.adress = adress
        self.contacts = contacts

    def change_data(self, key, value):
        """
        Changes the information in the current provider
        :param key: str
        :param value: str
        :return:
        """
        self.__dict__[key] = value

    def show_contacts(self):
        """
        Print the information about current provider
        :return:
        """
        print(f"Provider: {self.name}\n"
              f"Adress: {self.adress}\n"
              f"Contacts: {self.contacts}\n")
