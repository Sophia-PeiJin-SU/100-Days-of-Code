from turtle import Turtle, Screen
import random

game = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will be the winner? Enter a colour: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    y_direction = -60 + (30 * turtle_index)
    new_turtle.goto(x=-230, y=y_direction)
    all_turtles.append(new_turtle)

if user_bet:
    game = True

while game:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost... The {winner_color} turtle is the winner!")

        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)

screen.exitonclick()
