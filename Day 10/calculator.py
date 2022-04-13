# Day 10 of Angela Yu's "100 Days of Python" on udemy.

from art import logo
import os

print(logo)

# Math Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = { 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calulator Logic
def calculator():
    calculate = True
    num1 = float(input("What's the first number?:\n"))
    while calculate:
        operation_symbol = input("Pick an operation: + - * /: \n")
        num2 = float(input("What's the next number?: \n"))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # For future calculations
        num1 = answer
        response = input(f"Type 'Y' to continue calculating with {answer}, type 'N' to start a new calculation, or anything else to exit this application.\n").upper()
        if response == "Y":
            num1 = answer
        elif response == "N":
            calculate = False
            os.system("clear")
            calculator()
        else:
            calculate = False
            os.system("clear")

calculator()