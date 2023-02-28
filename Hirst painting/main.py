# import colorgram
# number_of_colors = 25
# colors = colorgram.extract("My image.jpg", number_of_colors)
# my_colors = []
#
#
# for item in range(number_of_colors):
#     rgb = colors[item].rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     new_color = (red, green, blue)
#     my_colors.append(new_color)
# print(my_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
final_colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setpos(-200, -200)


def line_painting():
    for _ in range(10):
        tim.dot(20, random.choice(final_colors))
        tim.forward(50)


def new_position():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


for _ in range(10):
    line_painting()
    new_position()










screen = Screen()
screen.exitonclick()