from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0

    def score_count(self):
        self.user_score += 1

    def scoreboard_update(self):
        self.clear()
        self.score_count()

    def end_game(self):
        self.penup()
        self.hideturtle()
        self.write("Congratulations! All states mapped!", align='center', font=('Arial', 24, 'normal'))


