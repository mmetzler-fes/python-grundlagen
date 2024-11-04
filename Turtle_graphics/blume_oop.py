from turtle import *
import random
import math
Turtle()

class Herz:
    def __init__(self, size, pencolor="red", fillcolor="red"):
        self.size=size
        self.pencolor=pencolor
        self.fillcolor=fillcolor
        self.x=100
        self.y=100
        self.angle=0
        
    def setPosition(self, x,y):
        self.x=x
        self.y=y
        
    def setWinkel(self, angle):
        self.angle=angle
        
    def draw(self):
        penup()
        setheading(self.angle)
        goto(self.x,self.y)
        pendown()
        hideturtle()
        pencolor(self.pencolor)
        fillcolor(self.fillcolor)
        begin_fill()
        left(45)
        circle(radius=self.size, extent=180, steps=20)
        right(90)
        circle(radius=self.size, extent=180, steps=20)
        forward(int(9/5*self.size))
        end_fill()
        penup()
        

class notenschluessel:
    def __init__(self, size, x, y):
        self.size=size
        self.x=y
        self.y=y
        
    def draw(self):
        step=self.size
        penup()
        right(30)
        goto(self.x,self.y)
        pendown()
        for i in range(0,260):
            pendown()
            right(10-8*i/100)
            forward(step)
            step=step+int(0.14*step)

def zufallsherzen():
    breite=window_width()
    hoehe=window_height()
    for i in range(10):
        size=20+random.randint(0,40)
        x=random.randint(size,breite-size-1)-int(breite/2)
        y=random.randint(size,hoehe-size-1)-int(hoehe/2)
        herz=Herz(size)
        herz.setPosition(x,y)
        herz.draw()


def blume():
    for j in range (0,360):
        x=40*math.sin(j*2*math.pi/360.0)
        y=40*math.cos(j*2*math.pi/360.0)
        schluessel=notenschluessel(5,int(x),int(y))
        schluessel.draw()
    
      
speed(0)
zufallsherzen()
