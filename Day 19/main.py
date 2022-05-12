# Etch-A-Sketch

from turtle import Turtle, Screen

t = Turtle()
t.shape("arrow")
t.speed(10)

screen = Screen()
screen.title("Etch-A-Sketch")

def move_forward():
    t.forward(10)
def move_back():
    t.back(10)
def clockwise_rotation():
    t.right(10)
def counter_clockwise_rotation():
    t.left(10)
def reset():
    t.reset()

screen.listen()

# Movement
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(clockwise_rotation, "d")
screen.onkey(counter_clockwise_rotation, "a")
screen.onkey(reset, "c")

screen.exitonclick()