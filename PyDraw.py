#PyDraw.py
import turtle
turtle.setup(650,350,100,100)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(3):
    turtle.circle(40,80)
    turtle.circle(-40,80)

turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()

