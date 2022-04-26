"""
Module demonstrates work with restaurant classes
"""
import json
import os
from classes import Waiter, Chef, Bill, Provider, Product, Menu, Dish
from classes import Restaurant, Card, Cash, Customer, Position

FILE_DATA = 'data.json'


def cls():
    """
    Clear terminal screen
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def dump_data(file_name, key):
    """
    Read JSON-file by key
    :param file_name: str
    :param key: str
    :return: dict
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data[key]


def init_data(cls_obj, item_key):
    """
    Creates dictionary of demo-classes using info from JSON-file
    :param cls_obj: class
    :param item_key: str
    :return: dict
    """
    objects = {}
    for item, value in dump_data(FILE_DATA, item_key).items():
        objects[item_key + '_' + item] = cls_obj(_id=item)
        for key, val in value.items():
            objects[item_key + '_' + item].change_data(key, val)
    return objects


if __name__ == '__main__':
    # ---------------------------INIT-------------
    print("\t\tPROVIDERS")
    providers = init_data(Provider, 'provider')
    for provider in providers.values():
        provider.show_contacts()
    input("Press enter to continue")

    print("\t\tPRODUCTS")
    products = init_data(Product, 'product')
    for product in products.values():
        product.show_product()
    input("Press enter to continue")

    print("\t\tDISHES")
    dishes = init_data(Dish, 'dish')
    for dish in dishes.values():
        dish.show_dish()
    input("Press enter to continue")

    print("\t\tMENU")
    menus = init_data(Menu, 'menu')
    for menu in menus.values():
        menu.show_menu()
    input("Press enter to continue")

    print("\t\tRESTAURANTS")
    restaurants = init_data(Restaurant, 'restaurant')
    for restaurant in restaurants.values():
        restaurant.show_data()
    input("Press enter to continue")

    print("\t\tCUSTOMERS")
    customers = init_data(Customer, 'customer')
    for customer in customers.values():
        customer.show_data()
    input("Press enter to continue")

    print("\t\tPOSITIONS")
    positions = init_data(Position, 'position')
    for position in positions.values():
        position.show_data()
    input("Press enter to continue")

    print("\t\tWAITERS")
    waiters = init_data(Waiter, 'waiter')
    for waiter in waiters.values():
        waiter.show_data()
    input("Press enter to continue")

    print("\t\tCHEFS")
    chefs = init_data(Chef, 'chef')
    for chef in chefs.values():
        chef.show_data()
    input("Press enter to continue")

    input("You are a customer. Press enter to see menu")
    for menu in menus.values():
        menu.show_menu()
    input("Press enter to continue")

    order_1 = customers["customer_1"].create_order()
    print()
    customers["customer_1"].inc_order(order_1, "Beer", 2, 35)
    customers["customer_1"].inc_order(order_1, "Fried potato with fish", 2, 55)
    order_1.show_order()
    print()
    bill = Bill(order_1)
    print(f"Your bill is: {bill.total} total")
    print("Choose payment (cash/card) >> card")
    payment = Card(bill)
    payment.pay()

    print()
    print("You are a waiter. Take an order")
    order_2 = waiters["waiter_1"].take_order()
    waiters["waiter_1"].show_data()
    waiters["waiter_1"].inc_order(order_2, "Salad", 3, 62)
    waiters["waiter_1"].inc_order(order_2, "Fresh juice", 3, 26)
    order_2.show_order()
    print()
    chefs["chef_1"].take_order(order_2)
    chefs["chef_1"].close_order(order_2)

    bill_2 = Bill(order_2)
    print(f"Your bill is: {bill_2.total} total")
    print("Choose payment (cash/card) >> cash")
    payment = Cash(bill_2)
    payment.pay()
    waiters["waiter_1"].close_order(order_2)
