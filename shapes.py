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
tdat.shape("turtle")
tdat.color("light blue")
colormode(255)
num_of_sides = 3


for step in range(3, 11):
    tdat.color(random_color())
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        tdat.forward(100)
        tdat.right(angle)
    num_of_sides += 1

screen = Screen()
screen.exitonclick()
