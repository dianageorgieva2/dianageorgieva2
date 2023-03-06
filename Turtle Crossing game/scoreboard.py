from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=280)
        self.level = 1
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f"Level: {self.level}")

    def next_level(self):
        self.level += 1
        self.clear()
        self.scoreboard_update()

    def exit(self):

        self.goto(0, 0)
        self.write("GAME OVER", align="center")
