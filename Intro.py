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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. create a function that ask the user what does it want

user_input = input("What would you like? (espresso/latte/cappuccino):\n").lower()

machine_active = True

# TODO: 2. create a function that do the report when asked to


def print_report():
    print(f'Water: {resources["water"]} ml\n Milk: {resources["milk"]} ml\n Coffee: {resources["coffee"]} ml')


print_report()







