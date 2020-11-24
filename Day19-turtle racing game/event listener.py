from turtle import Turtle, Screen

denny = Turtle()
denny.shape("turtle")
denny.color("coral")
screen = Screen()


def move_forward():
    denny.forward(10)


def move_backward():
    denny.backward(10)


def turn_left():
    denny.left(10)


def turn_right():
    denny.right(10)


def clear():
    denny.clear()
    denny.penup()
    denny.home()
    denny.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
