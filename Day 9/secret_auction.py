# Day 9 of Angela Yu's "100 Days of Python" on udemy.

import os
from art import logo
add_bidder = True
bids = {}

print(logo)
print("Welcome to the secret auction program.")

def highest_bidder(bids):
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while add_bidder:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system("clear")
    if more_bidders == "no":
        add_bidder = False

highest_bidder(bids)