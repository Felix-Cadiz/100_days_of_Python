# Day 12 of Angela Yu's "100 Days of Python" on udemy.

from multiprocessing.connection import answer_challenge
from random import randint

guesses = 0

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard':")

def difficulty():
    if level == "easy":
        guesses = 10
        return guesses
    elif level == "hard":
        guesses = 5
        return guesses
    else:
        print("Please input a valid response")
        # level = input("Choose a difficulty. Type 'easy' or 'hard':")
        # difficulty()

guesses = difficulty()
print(guesses)

answer = randint(1, 100)
print(answer)

print(f"You have {guesses} attempts remaining.")
attempt = int(input("Make a guess:\n"))

while not attempt == answer and guesses > 1:
    if attempt < answer:
        guesses -= 1
        print("Too low.")
        print(f"You have {guesses} attempts remaining.")
        attempt = int(input("Make a guess:\n"))
    elif attempt > answer:
        guesses -= 1
        print("Too high")
        print(f"You have {guesses} attempts remaining.")
        attempt = int(input("Make a guess:\n"))

if not attempt == answer and guesses == 1:
    print("You lose!")

if attempt == answer:
    print(f"You got it! The answer was {answer}")