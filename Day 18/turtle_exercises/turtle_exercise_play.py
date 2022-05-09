from turtle import Turtle, Screen
import random

t = Turtle()
# t.shape("turtle")
t.pensize(1)
t.speed("fastest")

s = Screen()
s.colormode(255)
s.bgcolor("black")

def color_param():
    r = int(random.randint(0,255))
    g = int(random.randint(0,255))
    b = int(random.randint(0,255))
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap_size):
    for i in range(1000):
        t.color(color_param())
        t.circle(i + 1)
        t.left(gap_size * 2)

draw_spirograph(2)

s.exitonclick()