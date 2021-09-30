from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
drinks_menu = Menu()
machine = CoffeeMaker()
power = True



while power == True:
    user_input = input(f"Hello! would you like a {drinks_menu.get_items()}")
    if user_input == 'report':
        machine.report()
        money.report()
    elif user_input == 'off':
        power = False
    else:
        order = drinks_menu.find_drink(user_input)
        if machine.is_resource_sufficient(order) and money.make_payment(order.cost):
            print('BOOM, lets grind beans')
            machine.make_coffee(order)
        else:
            print('low resources')
print('nightnight')

