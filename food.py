from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.new_foodini()

    def new_foodini(self):
        self.clear()
        random_x = random.randint(-400, 400)
        random_y = random.randint(-400, 400)
        self.goto(random_x, random_y)
        self.color(random.choice(colors))
