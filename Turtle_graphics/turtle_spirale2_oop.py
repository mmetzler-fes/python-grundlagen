from turtle import *

class Spirale():
    
    def __init__(self,size, windowsize, steps):
        self.size=size
        self.windowsize=windowsize
        self.steps=steps
        self.turtle=Turtle()
        
    def draw(self):
        min_windowsize = min(self.windowsize)
        x=min_windowsize/200
        for _ in range(self.steps):
            forward(x)
            right(10)
            x=x+0.1
            curx,cury=position()
            if abs(curx) > window_width()/2:
                break
            if abs(cury) > window_height()/2:
                break
            


window_size = (window_width(), window_height())
spirale=Spirale(1,window_size,600)
spirale.draw()
