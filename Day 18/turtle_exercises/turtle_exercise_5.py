from turtle import Turtle, Screen
import random

t = Turtle()
# t.shape("turtle")
t.pensize(1)
t.speed("fastest")

s = Screen()
s.colormode(255)

faces = [0, 90, 180, 270]

def color_param():
    r = int(random.randint(0,255))
    g = int(random.randint(0,255))
    b = int(random.randint(0,255))
    random_color = (r, g, b)
    return random_color

def direction():
    return faces[random.randint(0,3)]

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        t.color(color_param())
        t.circle(100)
        t.left(gap_size)

    for _ in range(int(360 / gap_size)):
        t.pensize(3)
        t.color(color_param())
        t.circle(100)
        t.right(gap_size)

draw_spirograph(5)

s.exitonclick()