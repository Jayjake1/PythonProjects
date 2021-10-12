# TODO print report
# TODO Resources sufficiency
# TODO Process coins
# TODO Check transaction successful

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(MENU['espresso'])


def is_resource_sufficient(drink_requirements):
    for items in drink_requirements:
        if drink_requirements[items] > resources[items]:
            print("Order cant be processes")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many rupees?: ")) * 1
    total += int(input("how many halfs?: ")) * 0.5
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many paisas?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is RS:{change}/- in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def make_coffee(choice, drink_requirements):
    """Deduct the required ingredients from the resources."""
    for item in drink_requirements:
        resources[item] -= drink_requirements[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


is_on = True


while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
