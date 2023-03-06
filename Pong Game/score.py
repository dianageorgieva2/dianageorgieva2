from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.pencolor("white")
        self.score_r = 0
        self.score_l = 0

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score_l} / {self.score_r}", align="center")

    def increase_score_r(self):
        self.score_r += 1
        self.score_update()

    def increase_score_l(self):
        self.score_l += 1
        self.score_update()

