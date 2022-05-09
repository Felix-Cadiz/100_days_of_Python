from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
counter = 0
box = 0

while counter < 40:
    timmy_the_turtle.forward(2)
    timmy_the_turtle.left(2)
    counter += 1
    box += 1
    if box % 4 == 0:
        timmy_the_turtle.left(45)
        timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()