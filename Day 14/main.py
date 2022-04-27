# Day 14 of Angela Yu's "100 Days of Python" on udemy.

from random import randint
from art import logo, vs
from game_data import data
import os

print(logo)

def index_pull():
    random_index = randint(0, 49)
    return data[random_index]

def fetchInfo(index):
    name = index["name"]
    follower_count = index["follower_count"]
    description = index["description"]
    country = index["country"]
    return [name, follower_count, description, country]

def guess_name(guess, a_info, b_info):
    if guess == "A":
        return a_info[0]
    else: 
        return b_info[0]

def compare(a_info, b_info):
    if a_info[1] > b_info[1]:
        return a_info[0]
    else:
        return b_info[0]

def reset():
    reset = input("Would you like to play again? 'Y' or 'N' \n").upper()
    if reset == "Y":
        initial()
    else:
        os.system("clear")

def initial():
    score = 0
    game_over = False
    a = index_pull()
    a_info = fetchInfo(a)
    game(a, a_info, score, game_over)

def game(a, a_info, score, game_over):
    b = index_pull()
    while a == b:
        b = index_pull()
    b_info = fetchInfo(b)
    print(f"Compare A: {a_info[0]}, a {a_info[2]}, from {a_info[3]}.")
    print(vs)
    print(f"Against B: {b_info[0]}, a {b_info[2]}, from {b_info[3]}.")
    guess = input("Who has more followers? Type 'A' or 'B': \n").upper()
    guess_result = guess_name(guess, a_info, b_info)
    winner = compare(a_info, b_info)
    os.system("clear")
    print(f"The winner is {winner}")

# Next round paramenters
    if guess_result == winner:
        score = score + 1
        print(f"You got it right!\nYour score is {score}")
    else:
        print(f"Sorry, you got it wrong\nYour final score is {score}")
        game_over = True

# Game over paramenters
    if game_over == False:
        a = b
        a_info = b_info
        game(a, a_info, score, game_over)
    else:
        reset()
        score = 0

initial()