from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

coffeeMaker.report()
moneyMachine.report()


isOn = True

while isOn:
    options = menu.get_items()
    chosen = input(f"What would you like? {options} ").lower()
    if chosen == "off":
        isOn = False
    elif chosen == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        chosenDrink = menu.find_drink(chosen)
        ingrEnough = coffeeMaker.is_resource_sufficient((chosenDrink))
        paidEnough = moneyMachine.make_payment(chosenDrink.cost)
        if ingrEnough and paidEnough:
            makeCoffee = coffeeMaker.make_coffee(chosenDrink)
