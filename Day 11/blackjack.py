import os
from art import logo
import random

start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':\n").upper()
if start:
    print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
add_card = ""
# hands = {
#     "player": [random.choice(cards), random.choice(cards)],
#     "computer": [random.choice(cards), random.choice(cards)],
# }
player_hand = [random.choice(cards), random.choice(cards)]
player_total = sum(player_hand)

computer_hand = [random.choice(cards), random.choice(cards)]
computer_total = sum(computer_hand)

def bust():
    if player_total > 21:
        return "You Lose!"

def add_card_function():
    if add_card == "Y":
        player_hand.append(random.choice(cards))
        player_total = sum(player_hand)
        print(f"Your current hand is: {player_hand}")
        print(player_total)
    elif add_card == "N":
        your_turn = "N"
        return

# def blackjack(): 
print(f"You cards are: {player_hand}")
print(f"Computer's first card: {computer_hand[0]}")
add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
while add_card == "Y":
    bust()
    add_card_function()
    add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
print(f"Your final hand: {player_hand}")
# print("Computer's final hand:")
# print("The winner is:")
# play_again = input("Do you want to play again? Type 'Y' or 'N':\n").upper()
# if play_again:
#     os.system("clear")
#     blackjack()