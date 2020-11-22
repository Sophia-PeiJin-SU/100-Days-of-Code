from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine = True
while machine:
    options = menu.get_items()
    coffee_ordered = input(f"What would you like? {options}: ")
    if coffee_ordered == "off":
        machine = False
    elif coffee_ordered == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_ordered)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
