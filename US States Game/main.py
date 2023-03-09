from turtle import Turtle, Screen
from states import State
from scoreboard import Scoreboard
import pandas
ALL_STATES = 50

screen = Screen()
turtle = Turtle()
states = State()
scoreboard = Scoreboard()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
states_to_learn = []

while scoreboard.user_score < ALL_STATES:
    answer_state =\
        screen.textinput(title=f"{scoreboard.user_score}/50 States correct", prompt="What's another state?").title()

    if answer_state == "Exit":
        for state in state_list:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        state_name = answer_state
        state_x = int(state_row.x)
        state_y = int(state_row.y)
        states.print_state_name(state_name, state_x, state_y)
        scoreboard.scoreboard_update()

if scoreboard.user_score == ALL_STATES:
    scoreboard.end_game()






