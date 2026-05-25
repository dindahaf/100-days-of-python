
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_running = True
profit = 0
while is_running:
    options = menu.get_items()
    response = input(f"What would you like? ({options}): ").lower()
    if response == "report":
        coffee_maker.report()
        money_machine.report()
    elif response == "off":
        is_running = False
    else:
        drink = menu.find_drink(response)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


