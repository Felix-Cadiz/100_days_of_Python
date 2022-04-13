# Day 10 of Angela Yu's "100 Days of Python" on udemy.

from art import logo

print(logo)
calculate = True

# Math Functions
def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    quotent = num1 / num2
    return quotent

def more_calculations(response):
    if not response == "Y":
        calculate = False

# Calulator Logic
first_digit = int(input("What's the first number?:\n"))
# response = input(f"Type 'Y' to continue calculating with {final}, or type 'N' to start a new calculation.").upper()

while calculate == True:
    operation = input("Pick an operation: + - * /: \n")
    second_digit = int(input("What's the next number?: \n"))
    if operation == "+":
        final = add(first_digit, second_digit)
        print(final)
        first_digit = final
        # more_calculations()
    elif operation == "-":
        final = subtract(first_digit, second_digit)
        print(final)
        first_digit = final
    elif operation == "*":
        final = multiply(first_digit, second_digit)
        print(final)
        first_digit = final
    elif operation == "/":
        final = divide(first_digit, second_digit)
        print(final)
        first_digit = final