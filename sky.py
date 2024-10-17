
import turtle as trtl
from turtle import Screen
screen = Screen()
cloud_gradient = ['steelblue','lightblue','powderblue','skyblue']

screen.colormode(255)
screen.screensize(canvwidth=800, canvheight=800)
painter = trtl.Turtle()
painter.speed(0)
painter.width(20)
global g
g = 255
global y
y = 239
global z
z = 213
def turtlecolor():
    global g
    global y
    global z
    y -= 1
    z -= 3
    g -= 1
    painter.color(g,y,z)

global h
h = 0

global x
x = 6

def sun():
    global x 
    for h in range(10):
        painter.penup()
        painter.goto(x/(x*x*x*x), x/(x*x*x))
        painter.pendown()
        turtlecolor()
        painter.circle(x)
        x += 6
        h += 1
##replace xcord and ycord w user input 
xcord = 0
ycord = 0
def cloud():
    global cloud_gradient
    global xcord
    global ycord
    trtl.speed(0)
    trtl.penup()
    trtl.goto(xcord,ycord)
    trtl.pendown()
    trtl.pensize(5)
    trtl.setheading(90)
    number_list = [10,-13,-14,15,-16,19,-15,-13,17,-16,14,12,17,18,19,13,13,15,16,19,23,24,-23,-19,26,23,13,14,15,16,19]
    restorer_list = [10,-13,-14,15,-16,19,-15,-13,17,-16,14,12,17,18,19,13,13,15,16,19,23,24,-23,-19,26,23,13,14,15,16,19]
    angle_list = [56,78,90,90,67,78,56,35,47,88,99,34,90,65,43,19,293,270,67,23,245,25,20]
    for row in range(4):
        pop = cloud_gradient.pop()
        trtl.fillcolor(pop)
        trtl.color(pop)
        for b in range(8):
            trtl.begin_fill()
            trtl.circle(30)
            trtl.end_fill()
            rand = number_list.pop()
            xcord+=rand
            rand = number_list.pop()
            ycord+=rand
            number_list.extend(list(restorer_list))
            trtl.penup()
            angle = angle_list.pop()
            trtl.setheading(angle)
            trtl.goto(xcord,ycord)
            trtl.pendown()
    xcord += 30
    ycord += 30
            
sun()
cloud()
cloud()
