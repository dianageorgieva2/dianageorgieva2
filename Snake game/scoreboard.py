from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 8, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # self.restart()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def restart(self):
        self.goto(0, -20)
        self.write("Do you want to play again - y or n?", align=ALIGNMENT, font=FONT)

