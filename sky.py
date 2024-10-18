
import turtle as trtl
from turtle import Screen
screen = Screen()
cloud1_gradient = ['powderblue', 'skyblue', 'lightblue','lightskyblue']

screen.colormode(255)
screen.screensize(canvwidth=800, canvheight=800)
t = trtl.Turtle()
t.speed(0)
t.width(45)


def sky():
    x = 6 
    h = 0 
    y = 255
    z = 239
    g = 213
    for h in range(40):
        t.penup()
        t.goto(x/(x*x*x*x), -300+x/(x*x*x))
        t.pendown()
        y -= 1
        z -= 3
        g -= 1
        t.color(y,z,g)
        t.circle(x)
        x += 20
        h += 1


def sun():
    x = 6 
    h = 0 
    y = 255
    z = 255
    g = 255
    for h in range(5):
        t.penup()
        t.goto(x/(x*x*x*x), x/(x*x*x))
        t.pendown()
        y -= 1
        z -= 3
        g -= 1
        t.color(y,z,g)
        t.circle(x)
        x += 20
        h += 1
xcord = 45
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
    xcord+=10
    ycord+=3
    trtl.goto(xcord,ycord)
    trtl.pendown()
    trtl.pensize(5)
    trtl.setheading(90)
    number_list = [10,-13,-14,25,-16,19,-15,-23,17,-16,24,12,-27,-18,-19,-13,-13,-15,-16,19,23,24,-23,-19,26,23,13,14,15,16,19]
    gg_list = [56,78,90,-90,67,-78,56,-35,47,-88,99,-34,30,-65,43,-19,293,-270,-67,23,245,25,20]
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

ohdear = input("would you like to see clouds?")
y = ["yes","y","Y","YES","Yes"]
if ohdear in y:
    sky()
    sun()
    cloud1()
    cloud2()
else:
    sky()
    sun()

trtl.done()