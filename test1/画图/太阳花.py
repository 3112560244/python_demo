import turtle
import time


turtle.penup()
turtle.forward(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.setheading(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.forward(40)

turtle.circle(16,180)
turtle.forward(40*2/3)
turtle.done()





