import random
import turtle

import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract("image.jpg", 20)
# tuples = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     tuples.append(new_color)
#
# print(tuples)

color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187)]
turtle.colormode(255)

tim = Turtle()
my_screen = Screen()
tim.color("blue")
tim.speed("fastest")

start_x_pos = -275
start_y_pos = -225
position_y_steps = 50
tim.penup()
tim.hideturtle()

tim.setpos(start_x_pos, start_y_pos)

for i in range(10):
    tim.setpos(start_x_pos, start_y_pos + i * position_y_steps)
    for j in range(10):
        tim.penup()
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

tim.shape("turtle")

my_screen.exitonclick()
