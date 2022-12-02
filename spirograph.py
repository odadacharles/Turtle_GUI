from turtle import *
from random import randint


def random_color():
    """ Returns a random RGB color as a tuple"""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color_choice = (red, green, blue)
    return color_choice


tdat = Turtle()
tdat.speed(0)
colormode(255)


def draw_spirograph(size_of_gap):
    for angle in range(int(360/size_of_gap)):
        tdat.color(random_color())
        tdat.circle(100)
        tdat.left(size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
