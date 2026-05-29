from pkgutil import extend_path
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed("fastest")

tim.forward(100)  # forward takes a number which is the distance to move
tim.right(90)  # turn right
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

for _ in range(4):
    tim.forward(100)
    tim.right(90)

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


pen_color = ["purple", "red", "green", "orange"]
def draw_polygon(polygon_sides):
    degree = 360 / polygon_sides
    for _ in range(polygon_sides):
        tim.forward(100)
        tim.right(degree)

for shape in range (3, 11):
    tim.color(random.choice(pen_color))
    draw_polygon(shape)

tim.left(90)
tim.left(90)
tim.forward(160)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    result = (r, g, b)
    return result

directions =[0, 90, 180, 270]
tim.pensize(15)
screen = Screen()
screen.colormode(255)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

tim.pensize(0)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)





screen.exitonclick()





