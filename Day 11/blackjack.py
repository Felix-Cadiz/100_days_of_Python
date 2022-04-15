#Day 10 of Angela Yu's "100 Days of Python" on udemy.

import os
import sys
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hands = {
    'player': [],
    'computer': [],
}

computer_total = sum(hands["computer"])

def restart():
    play_again = input("Do you want to play again? Type 'Y' or 'N':\n").upper()
    if play_again == "Y":
        os.system("clear")
        hands = {
            'player': [],
            'computer': [],
        }
        blackjack()
    else: 
        os.system("clear")
        sys.exit()

def bust(player_total):
    if player_total < 21:
        return
    print(f"BUST! You went over 21!\nYour hand total was {player_total}")
    restart()

def add_card_function(hands):
    hands['player'].append(random.choice(cards))
    player_total = sum(hands['player'])
    bust(player_total)
    for card in hands["player"]:
        if card == 11 and player_total > 22:
            card = 1
    print(f"Your current hand is: {hands['player']} for a total of {player_total}")
    return hands['player'], player_total

def winner(hands):
    player_total = sum(hands["player"])
    computer_total = sum(hands['computer'])
    if player_total > computer_total:
        return "You! Congratulations!"
    elif player_total == computer_total:
        return "Nobody!\nIt's a draw!"
    else:
        return "The Computer!\nBetter luck next time!"

def blackjack(): 
    hands = {
        'player': [random.choice(cards), random.choice(cards)],
        'computer': [random.choice(cards), random.choice(cards)],
    }
    player_total = sum(hands['player'])
    print(f"You cards are: {hands['player']}", "total =", player_total)
    print(f"Computer's first card: {hands['computer'][0]}")
    add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    while add_card == "Y":
        add_card_function(hands)
        add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    # print(f"Your final hand: {player_hand}")
    # print(f"The computer's final hand: {computer_hand}")
    # if computer_total <= 15:
    #     print("The computer needs more cards")
    # print("Computer's final hand: {computer_hand}")

    print(f"The winner is {winner(hands)}")
    restart()

start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':\n").upper()
if start == "Y":
    print(logo)
    blackjack()
else:
    os.system("clear")