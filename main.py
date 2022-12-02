from turtle import Turtle, Screen

tdat = Turtle()
tdat.shape("turtle")
tdat.color("light blue")


for step in range(10):
    tdat.forward(10)
    tdat.penup()
    tdat.forward(10)
    tdat.pendown()

screen = Screen()
screen.exitonclick()

