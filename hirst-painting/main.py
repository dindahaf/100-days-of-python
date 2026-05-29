# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# print(colors)
#
# color_palette = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     color_palette.append((r, g, b))
#
# print(color_palette)
color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)
t.penup()
t.hideturtle()
t.goto(-250, -250)
t.pendown()
for row in range(10):
    t.penup()
    t.goto(-250, -250 + (row * 50))
    t.pendown()
    for _ in range(9):
        t.dot(20,random.choice(color_list))
        t.penup()
        t.forward(50)
        t.pendown()
        t.dot(20,random.choice(color_list))

s.exitonclick()
