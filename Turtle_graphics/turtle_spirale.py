from turtle import *
def spirale(x):
    if (x<10):
        return
    forward(x)
    right(90)
    spirale(0.9*x)
    # rekursiver Aufruf
    return
spirale(200)
