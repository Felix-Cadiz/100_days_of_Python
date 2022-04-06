# Day 8 of Angela Yu's "100 Days of Python" on udemy.

# Globals and Starts
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

# Encrpt Logic
def encrypt(encode_path, initial_message, shift_amount):
    transformed_message = ""
    if encode_path == "decode":
        shift_amount *= -1
    for char in initial_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position =+ ((position + shift_amount) % 26)
            transformed_letter = alphabet[new_position]
            transformed_message += transformed_letter
        else:
            transformed_message += char
    print(f"The {encode_path}d text is '{transformed_message}'")

# Called Function
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(encode_path = direction, initial_message = message, shift_amount = shift)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if restart == "no":
        should_continue = False
        print("Thank you for using the Caesar Cipher")