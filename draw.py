import turtle
import random


obj=turtle.Turtle()

x=1

while x<400:
    obj.speed(10)
    wn=turtle.Screen()
    wn.bgcolor("black")
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.colormode(255)
    obj.pencolor(r,g,b)
    obj.pensize(1)
    obj.forward(10+x)
    obj.right(90.99)
    x=x+1
turtle.done()

    
    
    
