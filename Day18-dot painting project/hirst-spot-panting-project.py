import colorgram
from turtle import Turtle, Screen
import random

denny = Turtle()
denny.shape("turtle")
denny.color("SeaGreen4")

screen = Screen()
screen.colormode(255)
screen.colormode()

denny.speed("fastest")


# generate colors from an image
# colors = colorgram.extract('spotpainting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

denny.hideturtle()
for j in range(11):
    for i in range(10):
        denny.penup()
        random_color = random.choice(color_list)
        denny.dot(10, random_color)
        denny.forward(20)
    denny.home()
    denny.sety(20 * j)


screen.exitonclick()