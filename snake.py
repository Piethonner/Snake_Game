from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.additional_part(position)

    def additional_part(self, position):
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.goto(position)
        body_part.color("white")
        self.snake_body.append(body_part)

    def extend(self):
        self.additional_part(self.snake_body[-1].position())

    def move(self):
        for bod_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[bod_num - 1].xcor()
            new_y = self.snake_body[bod_num - 1].ycor()
            self.snake_body[bod_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
