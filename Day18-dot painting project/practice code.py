from turtle import Turtle, Screen
import random


denny = Turtle()
denny.shape("turtle")
denny.color("SeaGreen4")

screen = Screen()
screen.colormode(255)
screen.colormode()

denny.speed("fastest")
# denny.pensize(2)


def random_direction():
    num = random.randint(0, 1)
    if num == 0:
        return denny.left(90)
    else:
        return denny.right(90)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return denny.pencolor((r, g, b))


# challenge 1
# for i in range(4):
#     denny.forward(100)
#     denny.left(90)

# challenge 2
# for i in range(15):
#     denny.forward(5)
#     denny.penup()
#     denny.forward(5)
#     denny.pendown()

# challenge 3
# n = 0
# for j in range(5):
#     for i in range(3 + n):
#         denny.forward(100)
#         denny.left(360 / (3 + n))
#
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     denny.pencolor((r, g, b))
#     n += 1

# challenge 4
# for i in range(200):
#     denny.forward(20)
#     random_direction()
#     random_color()

# challenge 5
def draw_spiragraph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        denny.circle(100)
        random_color()
        current_heading = denny.heading()
        denny.setheading(current_heading + size_of_gap)


draw_spiragraph(5)

screen.exitonclick()
