# Creating a MENU dictionary with details of each type of drink and machine's resources
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# A function that will print the current resources in the machine
def get_report(money):
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: {money}")

# A function that will check available resources for a drink
def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if resources[ingredient] < MENU[choice]["ingredients"][ingredient]:
            print(f"Sorry there isn't enough {ingredient}")
            return False

# A function that will process that money inserted by the user
def process_coins(choice):
    print("Please insert coins.")
    quarter_coins = int(input("How many quarters?: "))
    dime_coins = int(input("How many dimes?: "))
    nickle_coins = int(input("How many nickles?: "))
    penny_coins = int(input("How many pennies?: "))
    total_inserted_money = float(round((quarter_coins * 0.25 + dime_coins * 0.1 + nickle_coins * 0.05 + penny_coins * 0.01), 2))
# Check whether the inserted money is enough to dispense the chosen drink and tender change if required
    if total_inserted_money < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change_left = round(total_inserted_money - MENU[choice]["cost"], 2)
        print(f"Here is ${change_left} in change. ")
        return MENU[choice]["cost"]

# Defining global variables
is_machine_off = False
MONEY = 0
while not is_machine_off:

# Prompt user by asking what would they like
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        get_report(MONEY)

# Call functions to perform resources and money checks, and dispense coffee if everything looks good
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        sufficient_resources = check_resources(user_choice)
        if sufficient_resources is not False:
            valid_amount = process_coins(user_choice)
            if valid_amount is not False:
                print(f"Here is your {user_choice}. Enjoy!")
                for menu_ingredient in MENU[user_choice]["ingredients"]:
                    resources[menu_ingredient] -= MENU[user_choice]["ingredients"][menu_ingredient]
                MONEY += valid_amount

# Turn off the coffee machine for maintenance
    elif user_choice == "off":
        is_machine_off = True

    else:
        print("Please enter a valid choice.")
