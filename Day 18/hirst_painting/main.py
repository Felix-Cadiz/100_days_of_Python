# Day 17 of Angela Yu's "100 Days of Python" on udemy.

from turtle import Turtle, Screen
from colors import Colors
import random

t = Turtle()
t.shape("turtle")
t.speed(100)
t.hideturtle()

screen = Screen()
screen.colormode(255)
screen.bgcolor("#000000")

dimensions = 10

color = Colors()
color_pallet = [(16, 28, 59), (63, 79, 136), (45, 20, 51), (43, 53, 107), (125, 69, 121), (112, 107, 179), (91, 43, 94), (145, 135, 208), (170, 95, 162), (187, 126, 184)]

def restart():
    t.home()
    t.penup()
    t.setheading(225)
    t.forward(330)
    t.setheading(0)
    t.clear()
    motor()
    restart()

def motor():
    for _ in range(dimensions):
        dot_maker()
        vertical_movement()

def vertical_movement():
        t.left(90)
        t.forward(50)
        t.right(90)

def dot_maker():
    for _ in range(dimensions):
        t.pendown()
        # t.dot(20, color.random_colors())
        t.dot(20, color_pallet[random.randint(0, 9)])
        t.penup()
        t.forward(50)
    t.back(500)

restart()

screen.exitonclick()