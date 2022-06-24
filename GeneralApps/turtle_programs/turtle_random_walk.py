from turtle import Turtle, Screen
import random 

my_turtle = Turtle()
screen = Screen()

colors = ['Blue', 'Green','Yellow','Violet','Red','Orange','Purple']
directions = [0,90,180,270]
my_turtle.shape("turtle")
my_turtle.pensize("15")

for _ in range(200):
    my_turtle.color(random.choice(colors))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))


screen.exitonclick()   