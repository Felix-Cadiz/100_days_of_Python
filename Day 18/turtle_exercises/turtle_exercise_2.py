# Create a dotted line

from turtle import Turtle, Screen

tom = Turtle()
tom.shape("classic")
tom.color("purple")

for _ in range(30):
    tom.forward(10)
    if tom.isdown():
        tom.penup()
    else:
        tom.pendown()
    
s = Screen()
s.exitonclick()