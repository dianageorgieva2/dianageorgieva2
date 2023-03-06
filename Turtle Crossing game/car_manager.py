from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle("square")
            car.hideturtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            y_position = random.randint(-250, 250)
            car.goto(x=300, y=y_position)
            car.showturtle()
            self.cars_list.append(car)

    def car_movement(self):
        for item in self.cars_list:
            if self.xcor() > -320:
                item.forward(self.car_speed)

    def level_speed(self):
        self.car_speed += MOVE_INCREMENT
