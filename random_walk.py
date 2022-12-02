from turtle import *
from random import randint
import random


def random_color():
    """ Returns a random RGB color as a tuple"""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color_choice = (red, green, blue)
    return color_choice


tdat = Turtle()
tdat.shape("turtle")
tdat.color("green")
colormode(255)
directions = [0, 90, 180, 270]
tdat.width(5)
tdat.speed("fastest")


for step in range(200):
    tdat.color(random_color())
    tdat.setheading(random.choice(directions))
    tdat.forward(50)

screen = Screen()
screen.exitonclick()
