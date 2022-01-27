from turtle import *

color('black','green')
shape('turtle')
pensize(5)
speed(1)




def makeShape (numSides):
    for i in range(numSides):
        forward(100)
        left(360.0/numSides)
        i += 1
        

for i in range(3,13):
    makeShape(i)
