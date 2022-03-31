# Day 6 of Angela Yu's "100 Days of Python" on udemy.

# Problem solving with Reeborg's World, a web based application that 
# trains its users the basics of functional Python.
# Link to final exercise:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Default commands in Reeborg's World

def move():
    print("Used to move forward one space.")
def turn_left():
    print("Used to turn Reeborg to the left.")
def at_goal():
    print("Used to check if Reeborg is at the 'completed' tile.")
def right_is_clear():
    print("Used to check if there is a wall to the right of Reeborg.")
def front_is_clear():
    print("Used to check if there is a wall in front of Reeborg.")

# Solution to maze problem:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left
    turn_left
    
while front_is_clear():
    move()
    
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()