# Day 12 of Angela Yu's "100 Days of Python" on udemy.

from random import randint
from art import logo
import os

# Game Setup
print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
EASY_MODE = 10
HARD_MODE = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").upper()
    if level == "EASY":
        return EASY_MODE
    else:
        level == "HARD"
        return HARD_MODE

# Game Logic
def game():
    guesses = difficulty()
    answer = randint(1, 100)
    print(f"You have {guesses} attempts remaining.")
    attempt = int(input("Make a guess:\n"))
    while not attempt == answer and guesses > 1:
        if attempt < answer: 
            guesses -= 1
            print(f"Too low.\nYou have {guesses} attempts remaining.")
            attempt = int(input("Make a guess:\n"))
        elif attempt > answer: 
            guesses -= 1
            print(f"Too high.\nYou have {guesses} attempts remaining.")
            attempt = int(input("Make a guess:\n"))
    if not attempt == answer and guesses == 1:
        print(f"You lose!\nThe answer was {answer}")
        reset()
    else:
        print(f"You got it! The answer was {answer}")
        reset()

def reset():
    play_again = input("Would you like to play again? 'Y' or 'N':\n").upper()
    if play_again == "Y":
        game()
    else:
        os.system("clear")

game()