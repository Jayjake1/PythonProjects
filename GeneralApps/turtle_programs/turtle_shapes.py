from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.color('green')

def shapes(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for values in range(3,10):
    shapes(values)

screen.exitonclick()  