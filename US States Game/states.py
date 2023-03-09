from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")

    def print_state_name(self, state_name, state_x, state_y):
        self.goto(x=state_x, y=state_y)
        self.write(state_name)

