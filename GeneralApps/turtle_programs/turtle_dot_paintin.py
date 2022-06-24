from turtle import Turtle, Screen
import turtle as t
import random
baby_turtle = Turtle()
baby_turtle.shape("turtle")
baby_turtle.color("purple")
baby_turtle.speed(50)
# baby_turtle.pensize(5)
t.colormode(255)

# color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink",'black']
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colored = (r,g,b)
    return colored

direction_list = [0,90,180,270]
# random walker 😅
for i in range(150):
    baby_turtle.color(random_color())
    baby_turtle.circle(100)
    baby_turtle.setheading(baby_turtle.heading()+5) #turtle.heading()
    
    

#screen for drawing a square
small_screen = Screen()
small_screen.bgcolor("white")
small_screen.title("A Turtle's Journey")
small_screen.exitonclick()