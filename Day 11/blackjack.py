#Day 10 of Angela Yu's "100 Days of Python" on udemy.

import os
import sys
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []
bust = False

def restart():
    play_again = input("Do you want to play again? Type 'Y' or 'N':\n").upper()
    if play_again == "Y":
        os.system("clear")
        print(logo)
        player = []
        computer = []
        blackjack()
    else: 
        os.system("clear")
        sys.exit()

def bust(total):
    if total < 22:
        return
    bust = True
    return bust, total

def deal_card():
    card = random.choice(cards)
    return card

def ace(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        print(hand)
        return sum(hand)
    else:
        return sum(hand)

def deal(player, player_total):
    player.append(random.choice(cards))
    # player_total = sum(player)
    player_total = ace(player)
    if bust(player_total):
        print (f"BUST! You went over 21!")
        restart()
    print(f"Your current hand is: {player} for a total of {player_total}")
    return player, player_total

def winner(player_total, computer_total):
    if player_total > computer_total:
        return "You! Congratulations!"
    elif player_total == computer_total:
        return "Nobody!\nIt's a draw!"
    else:
        return "The Computer!\nBetter luck next time!"

def blackjack(): 
    player = [deal_card(), deal_card()]
    computer = [deal_card(), deal_card()]
    player_total = sum(player)
    computer_total = sum(computer)
    print(f"You cards are: {player}, totalling {player_total}")
    print(f"Computer's first card: {computer[0]}")
    add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    while add_card == "Y":
        deal(player, player_total)
        add_card = input("Type 'y' to get another card, type 'n' to keep your hand:\n").upper()
    print(f"With a total of {player_total}, your final hand is {player}")
    while computer_total < 17:
        computer.append(deal_card())
        computer_total = sum(computer)
        if bust(computer_total):
            print(f"With a total of {computer_total}, the computer's final hand is {computer}")
            print (f"BUST! The computer went over 21!")
            restart()
    print(f"With a total of {computer_total}, the computer's final hand is {computer}")
    print(f"The winner is {winner(player_total, computer_total)}")
    print("player", player_total, "computer", computer_total)
    restart()

start = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':\n").upper()
if start == "Y":
    print(logo)
    blackjack()
else:
    os.system("clear")