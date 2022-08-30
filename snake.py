from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in POSITIONS:
            snake_body = Turtle(shape="square")
            snake_body.penup()
            snake_body.goto(position)
            snake_body.color("white")
            self.snake.append(snake_body)

    def move(self):
        for bod in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[bod - 1].xcor()
            new_y = self.snake[bod - 1].ycor()
            self.snake[bod].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

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
