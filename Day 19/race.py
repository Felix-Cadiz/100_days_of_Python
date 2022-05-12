from turtle import Turtle, Screen
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

screen = Screen()

movement_speed = random.randint(1, 10)

def start():
    #penup()
    pass

def race():
    pass

def reset():
    pass

screen.listen()

screen.onkey(start, "r")
screen.onkey(race, "space")
screen.onkey(reset, "w")




screen.exitonclick