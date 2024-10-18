
import turtle as trtl
from turtle import Screen
screen = Screen()
cloud1_gradient = ['steelblue', 'skyblue', 'lightblue','powderblue']

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
def cloud1():
    global cloud1_gradient
    global xcord
    global ycord
    trtl.speed(0)
    trtl.penup()
    trtl.goto(xcord,ycord)
    trtl.pendown()
    trtl.pensize(5)
    trtl.setheading(90)
    number_list = [10,-13,-14,15,-16,19,-15,-13,17,-16,14,12,-17,-18,-19,-13,-13,-15,-16,19,23,24,-23,-19,26,23,13,14,15,16,19]
    angle_list = [56,78,90,-90,67,-78,56,-35,47,-88,99,-34,90,-65,43,-19,293,-270,-67,23,-245,25,20]
    for row in range(2):
        pop = cloud1_gradient.pop()
        trtl.fillcolor(pop)
        trtl.color(pop)
        for b in range(7):
            trtl.begin_fill()
            trtl.circle(30)
            trtl.end_fill()
            rand = number_list.pop()
            xcord+=rand
            rand = number_list.pop()
            ycord+=rand
            trtl.penup()
            angle = angle_list.pop()
            trtl.setheading(angle)
            trtl.goto(xcord,ycord)
            trtl.pendown()
        row+=1
   

def cloud2():
    global cloud1_gradient
    global xcord
    global ycord
    trtl.speed(0)
    trtl.penup()
    xcord+=40
    ycord+=67
    trtl.goto(xcord,ycord)
    trtl.pendown()
    trtl.pensize(5)
    trtl.setheading(90)
    number_list = [10,-13,-14,15,-16,19,-15,-13,17,-16,14,12,-17,-18,-19,-13,-13,-15,-16,19,23,24,-23,-19,26,23,13,14,15,16,19]
    gg_list = [56,78,90,-90,67,-78,56,-35,47,-88,99,-34,90,-65,43,-19,293,-270,-67,23,245,25,20]
    for row in range(2):
        pop = cloud1_gradient.pop()
        trtl.fillcolor(pop)
        trtl.color(pop)
        for b in range(7):
            rand = number_list.pop()
            xcord+=rand
            rand = number_list.pop()
            ycord-=rand
            trtl.begin_fill()
            trtl.circle(30)
            trtl.end_fill()
            trtl.penup()
            angle = gg_list.pop()
            trtl.setheading(-angle*3)
            trtl.goto(-xcord,-ycord)
            trtl.pendown()
        row+=1
   
sun()
cloud1()
cloud2()
