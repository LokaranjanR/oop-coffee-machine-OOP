from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




menu = Menu()
makec = CoffeeMaker()
paisa = MoneyMachine()



while True:
    name = input("What would you like to order?(espresso/latte/cappuccino)")

    if name == "report" :
        makec.report() , paisa.report()
    elif name == "espresso":
        drinkval = menu.find_drink(name)
        if makec.is_resource_sufficient(drinkval) == True :

            paisa.make_payment(menu.get_cost(name))
            makec.make_coffee(menu.find_drink(name))
        else:
            print("There are not resources in the machine to make ypur order")
    elif name == "latte":
        drinkval = menu.find_drink(name)
        if makec.is_resource_sufficient(drinkval) == True:

            paisa.make_payment(menu.get_cost(name))
            makec.make_coffee(menu.find_drink(name))
        else:
            print("There are not resources in the machine to make ypur order")

    elif name == "cappuccino":
        drinkval = menu.find_drink(name)
        if makec.is_resource_sufficient(drinkval) == True:

            paisa.make_payment(menu.get_cost(name))
            makec.make_coffee(menu.find_drink(name))
        else:
            print("There are not resources in the machine to make ypur order")

    elif name == "stop":
        exit(0)
