import os
from art import logo
import random

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
        print(f"Your current hand is: {player_hand} for a total of {player_total}")

def winner():
    player_total = sum(player_hand)
    print(player_total)
    computer_total = sum(computer_hand)
    if player_total > computer_total:
        return "You! Congratulations!"
    elif player_total == computer_total:
        return "Nobody!\nIt's a draw!"
    else:
        return "The Computer!\nBetter luck next time!"

def blackjack(): 
    print(f"You cards are: {player_hand}")
    print(f"Computer's first card: {computer_hand[0]}")
    player_total = sum(player_hand)
    add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    while add_card == "Y":
        add_card_function()
        add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    print(f"Your final hand: {player_hand}")
    print(f"The computer's final hand: {computer_hand}")
    if computer_total <= 15:
        print("The computer needs more cards")
    # print("Computer's final hand: {computer_hand}")

    print(f"The winner is {winner()}")
    play_again = input("Do you want to play again? Type 'Y' or 'N':\n").upper()
    if play_again == "Y":
        os.system("clear")
        blackjack()
    else: 
        os.system("clear")

start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':\n").upper()
if start == "Y":
    print(logo)
    blackjack()
else:
    os.system("clear")

# for cards in hand:
#     if hand[i] == 11 and hand_total > 21:
#         hand[i] = 1