from turtle import Turtle, Screen
from colors import Colors
# from hirst_brain import HirstBrain

t = Turtle()
t.shape("turtle")
t.speed(100)
t.hideturtle()

screen = Screen()
screen.colormode(255)
screen.bgcolor("#000000")

dimensions = 7

color = Colors()

def restart():
    t.clear()
    t.home()
    motor()
    restart()

def motor():
    for i in range(dimensions):
        dot_maker()
        t.home()
        vertical_movement(i + 1)

def vertical_movement(line):
        t.left(90)
        t.forward(line * 50)
        t.right(90)

def dot_maker():
    for _ in range(dimensions):
        t.pendown()
        t.fillcolor(color.random_colors())
        t.dot(20, color.random_colors())
        t.penup()
        t.forward(50)

restart()

screen.exitonclick()