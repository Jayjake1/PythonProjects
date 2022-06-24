from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.color('green')
for i in range(20):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(5)

screen.exitonclick()