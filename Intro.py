MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
machine_active = True
user_choice = []

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 4. Check if resources are enough

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is no more {item}')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("insert coins")
    total = int(input('How many quarters?\n')) * 0.25
    total += int(input('How many nickels?\n')) * 0.05
    total += int(input('How many pennies?\n')) * 0.01
    return total


# TODO: 5 Check if transaction is successful

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded")
        return False


# TODO: 6 Make the beverage and reduce resources based on the user's choice
def make_beverage(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your drink {drink_name} ☕️, enjoy!')


def print_report():
    print(f'Water: {resources["water"]} ml\n Milk: {resources["milk"]} ml\n Coffee: {resources["coffee"]} ml')


# TODO: 1. create a function that ask the user what does it want

while machine_active:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_active = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_beverage(choice, drink["ingredients"])


