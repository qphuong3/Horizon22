from turtle import *
import random

speed(200)
bgcolor("black")
def randomPlace():
    x = random.randint(-250, 250)
    y = random.randint(-250,250)
    penup()
    goto(x,y)
    pendown()
def circles():
    for i in range(30):
        randomPlace()
        pencolor("white")
        circle(2*i)
        circle(-2*i)
    for i in range(8):
        randomPlace()
        fillcolor("white")
        begin_fill()
        circle(2*i)
        end_fill()
        randomPlace()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color(r,g,b)
        width(random.randint(1, 4))
        length = random.randint(10,40)
        for x in range(3):
            forward(length)
            left(120)
        randomPlace()
        begin_fill()
        for x in range(3):
            forward(length)
            left(120)
        end_fill()
        width(1)
        pencolor("white")
def drawFireworks():
    randomPlace()
    size = random.randint(10, 50)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color(r,g,b)
    for x in range(36):
        circle(size)
        left(10)

def drawSpiral():
    r, g, b = 255, 0, 0
    for i in range(510):
        colormode(255)
        if i < 255//3:
            g += 3
        elif i < (255*2)//3:
            r -= 3
        elif i < 255:
            b += 3
        elif i < (255*4)//3:
            g -= 3
        elif i < (255*5)//3:
            r += 3
        else:
            b -= 3
        fd(50+i)
        rt(91)
        pencolor(r, g, b)
color("white")
for i in range(100):
    circle(i*2)
    right(5)
def triangle (length , turn):
    if length > 0:
        forward(length)
        right(turn)
        triangle(length - 5, turn)
goto(20,0)
triangle (400,121)
goto(10,10)
drawSpiral()
for x in range(random.randint(2,3)):
    circles()
for x in range(random.randint(10,30)):
    drawFireworks()

exitonclick()