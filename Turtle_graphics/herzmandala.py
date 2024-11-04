from turtle import *
import random
Turtle()

def herz(groesse, fgcolor="black", bgcolor="red"):
    winkel=heading()
    x=xcor()
    y=ycor()
    hideturtle()
    pencolor(fgcolor)
    fillcolor(bgcolor)
    begin_fill()
    left(45)
    forward(int(9/5*groesse))
    circle(radius=groesse, extent=180, steps=20)
    right(90)
    circle(radius=groesse, extent=180, steps=20)
    goto(x,y)
    end_fill()
    setheading(winkel)

speed(0)
for i in range(24):
    winkel=int(360/24)
    forward(20)
    herz(10)
    right(winkel)
    forward(20)


