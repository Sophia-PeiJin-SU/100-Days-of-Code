from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segements.append(new_segment)

    def extend(self):
        self.add_snake(self.segements[-1].position())

    def move(self):
        for snake_num in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[snake_num - 1].xcor()
            new_y = self.segements[snake_num - 1].ycor()
            self.segements[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
