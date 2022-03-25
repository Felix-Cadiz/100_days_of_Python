# Day 4 of Angela Yu's "100 Days of Python" on udemy.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play Rock, Paper, Scissors!")
images = [rock, paper, scissors]

# User Input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
valid_user_input = (user == 0 or user == 1 or user == 2)

if(valid_user_input):
    print(images[user])
    # Computer Logic
    computer = random.randint(0,2)
    print("Computer chose:")
    print(images[computer])

# Results
print("And the winner is?")
if not(valid_user_input):
    print("The Computer!\nYou are disqualified for trying to cheat the game!")
elif(user == computer):
    print("Nobody! It's a draw!\nPlay again?")
elif((user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0)):
    print("The Computer!\nPlay again?")
elif((user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1)):
    print("You! Congratulations\nPlay again?")