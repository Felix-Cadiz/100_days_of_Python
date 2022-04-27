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
    print(f"You submitted ${paymentSum}")
    return paymentSum

def transaction(drink, paymentSum):
    if MENU[drink]["cost"] > paymentSum:
        print("Insufficient Funds.\nMoney refunded.")
        return False
    elif MENU[drink]["cost"] == paymentSum:
        make_coffee()
        # Add funds to money
        # Make Coffee function
        return True
    else:
        change = paymentSum - MENU[drink]["cost"]
        # Add funds to money
        # Make Coffee function
        return True

def make_coffee(drink):
    print("Fix this")

def selection(drink):
    if drink == "off":
        os.system("clear")
    elif drink == "report":
        print(resources)
        print(money)
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        print("checking resources")
        pay = payment()
        if transaction(drink, pay) == True:
            make_coffee(drink)
        reset()

reset()