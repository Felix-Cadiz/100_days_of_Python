# Day 5 of Angela Yu's "100 Days of Python" on udemy.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

print("Welcome to the PyPassword Generator!")

password_letters = int(input("How many letters would you like in your password?\n"))
for password_letter in range (1, password_letters + 1):
    password_letter = random.randint (0, len(letters) - 1)
    password.append(letters[password_letter])

password_symbols = int(input("How many symbols would you like?\n"))
for password_symbol in range (1, password_symbols + 1):
    password_symbol += random.choice(symbols)
    password.append(symbols[password_symbol])

password_numbers = int(input("How many numbers would you like?\n"))
for password_number in range(1, password_numbers + 1):
    password_number = random.randint (0, len(numbers) - 1)
    password.append(numbers[password_number])

print(len(password))
print(password)

random.shuffle(password)
print(password)


print(f"Here is your password: {password}")