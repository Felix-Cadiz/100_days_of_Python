# Day 3 of Angela Yu's "100 Days of Python" on udemy.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

path = input('After arriving to Treasure Island, you arrive at a crossroad. Where do you want to go? Type "Left" or "Right"\n').lower()
if(path == "right"):
    lake = input('After taking the right path, you come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').lower()
    if(lake == "wait"):
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n").lower()
        if(door == "red"):
            print("You found the treausre!\nYou Win!")
        elif(door == "yellow"):
            print("You enter a room full of beasts.\nGame Over")
        elif(door == "blue"):
            print("It's a room full of fire.\nGame Over")
        else:
            print("You chose a door that doesn't exist.\nGame Over")
    elif(lake == "swim"):
        print("You get attacked by an angry trout.\nGame Over")
    else:
        print("You stepped on a poisonous typo\nGame Over.")
elif(path == "left"): 
    print('You fall into a hold.\nGame Over.')
else:
    print("A wild typo hit you in the head and knocked you unconscious\nGame Over")
