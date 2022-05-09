from turtle import Turtle, Screen

tommy_turtle = Turtle()
tommy_turtle.shape("arrow")
tommy_turtle.color("blue")

for _ in range(4):
    tommy_turtle.forward(100)
    tommy_turtle.right(90)

screen = Screen()
screen.exitonclick()