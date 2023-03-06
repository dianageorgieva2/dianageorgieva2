import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
GAME_LEVELS = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_ahead, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.car_movement()

    if player.ycor() > 280:
        GAME_LEVELS -= 1
        car_manager.level_speed()
        if GAME_LEVELS < 1:
            scoreboard.exit()
            game_is_on = False
        else:
            scoreboard.next_level()
            player.starting_position()

    for item in car_manager.cars_list:
        if player.distance(item) < 20:
            scoreboard.exit()
            game_is_on = False

screen.exitonclick()
