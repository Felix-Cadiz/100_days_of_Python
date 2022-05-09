# Create a variety of polygons that change color with each iteration.

from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("turtle")
sides = 3

s = Screen()
s.colormode(255)

def color():
    return int(random.randint(1, 255))

for _ in range(8):
    tom.color(color(), color(), color())
    for _ in range(sides):
        tom.forward(100)
        tom.right(360/sides)
    sides += 1

s.exitonclick()