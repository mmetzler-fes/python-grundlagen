from turtle import *
import random
Turtle()

def herz(groesse, color="red"):
    winkel=heading()
    x=xcor()
    y=ycor()
    hideturtle()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    left(45)
    circle(radius=groesse, extent=180, steps=20)
    right(90)
    circle(radius=groesse, extent=180, steps=20)
    forward(int(9/5*groesse))
    goto(x,y)
    end_fill()
    setheading(winkel)

def vieleck(ecken, groesse=20):
    winkel=int(360/ecken)
    for i in range(ecken):
        forward(groesse)
        right(winkel)

def zufallsherzen():
    breite=window_width()
    hoehe=window_height()
    for i in range(10):
        x=random.randint(40,breite-41)-int(breite/2)
        y=random.randint(40,hoehe-41)-int(hoehe/2)
        penup()
        goto(x,y)
        pendown()
        herz(20)
        penup()

speed(0)
zufallsherzen()
home()
farben=["red","yellow","blue","pink","green","orange","brown"]
for i in range(320):
    farbe=farben[i%6]
    pencolor(farbe)
    vieleck(4,200)
    penup()
    right(5)
    forward(int(i/4))
    pendown()
    
    
