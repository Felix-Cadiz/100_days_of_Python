# Day 15 of Angela Yu's "100 Days of Python" of udemy.

from data import MENU, resources
import os

# print(MENU)
# print(resources)

money = 0

def reset():
    drink = input("Would you like an espresso, latte, or cappuccino?\n").lower()
    selection(drink)

def payment():
    quarters = int(input("Input Quarters: ")) * 0.25
    dimes = int(input("Input Dimes: ")) * 0.1
    nickles = int(input("Input Nickles: ")) * 0.05
    pennies = int(input("Input Pennies: ")) * 0.01
    paymentSum = round(quarters + dimes + nickles + pennies, 2)
    print(f"You submitted ${paymentSum:.2f}")
    return paymentSum

def transaction(drink, payment_sum):
    if MENU[drink]["cost"] > payment_sum:
        print("Insufficient Funds.\nMoney refunded.")
        return False
    else:
        global money
        if payment_sum > MENU[drink]["cost"]:
            change = payment_sum - MENU[drink]["cost"]
            print(f"Thank you for purchasing, please accept your ${change:.2f} in change.")
        money += round(MENU[drink]["cost"], 2)
        print(f"The machine now has ${money:.2f}")
        return True

def resource_check(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Not enough water")
        return False
    if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee")
        return False
    if drink == "latte" or drink == "cappuccino":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Not enough milk")
            return False
    return True

def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    print(f"Here is your {drink}, please enjoy!")

def selection(drink):
    if drink == "off":
        os.system("clear")
    elif drink == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        print(f"Money: ${money:.2f}")
        reset()
    elif MENU[drink]:
        print("checking resources")
        if resource_check(drink):
            print("Please insert coins:")
            payment_sum = payment()
            if transaction(drink, payment_sum) == True:
                make_coffee(drink)
                reset()
        else: 
            reset()

reset()