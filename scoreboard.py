from turtle import Turtle
ALIGN_VAL = "center"
FONT_VAL = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=420)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN_VAL, font=FONT_VAL)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGN_VAL, font=FONT_VAL)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
