from turtle import *
import random
import math
Turtle()

class Zeichenobjekt:
    def __init__(self, size, pencolor="red", fillcolor="red"):
        self.size=size
        self.pencolor=pencolor
        self.fillcolor=fillcolor
        self.x=100
        self.y=100
        self.angle=0

    def setposition(self, x,y):
        self.x=x
        self.y=y
        
    def setheading(self, angle):
        self.angle=angle


class Herz(Zeichenobjekt):
    def __init__(self, size, pencolor="red", fillcolor="red"):
        super().__init__(size, pencolor, fillcolor)
        
        
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
        goto(x,y)
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
        winkel=random.randint(0,359)
        herz=Herz(size)
        herz.setposition(x,y)
        herz.setheading(winkel)
        herz.draw()

def herzentabelle():
    breite=window_width()
    hoehe=window_height()
    color=["red","blue","green","purple","orange","pink","yellow","brown"]
    for i in range(0,5):
        x=breite/2-i*breite/5
        for j in range(0,5):
            indexcolor=random.randint(0,len(color)-1)
            y=hoehe/2-j*hoehe/5
            size=6+random.randint(0,8)
            winkel=random.randint(0,359)
            herz=Herz(size,color[indexcolor],color[indexcolor])
            herz.setposition(x,y)
            herz.setheading(winkel)
            herz.draw()
            

herzentabelle()
#zufallsherzen()