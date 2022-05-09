# Random walk with increased speed, width, and random colors.

from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.pensize(7)
t.speed(9)

s = Screen()
s.colormode(255)

move = True
faces = [0, 90, 180, 270]

def color_param():
    r = int(random.randint(0,255))
    g = int(random.randint(0,255))
    b = int(random.randint(0,255))
    random_color = (r, g, b)
    return random_color

def direction():
    return faces[random.randint(0,3)]

for _ in range(200):
    t.color(color_param())
    t.right(direction())
    t.forward(30)

s.exitonclick()