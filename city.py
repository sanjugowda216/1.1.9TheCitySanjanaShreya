import turtle as trtl
from turtle import Screen
screen = Screen()
screen.screensize(canvwidth=800, canvheight=800)

t = trtl.Turtle()
t.width(45)
t.speed(0)
screen.colormode(255)
cloud1_gradient = ['powderblue', 'skyblue', 'lightblue','lightskyblue']
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
    trtl.width(45)
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
    trtl.width(45)
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

building_gradient = ['black','gray','darkgray']
building_line = ['black','gray','darkgray']
building_height = [390,410,320,330,210,200,190,210,220,210,250,390,220,320,330,210,200,190,210,200,190,180,210,220,210,200,190,210,220,350,210,190,200,320,330,210,200,190,210,170,180,320,390,210,320,330,210,200,190,210,370,350,400]
building_width = [45,47,49,50,55,60,47,56,45,47,49,50,55,60,80,82,85,90,95,97,45,47,49,50,55,60,80,82,45,47,49,50,55,60,80,82,85,90,95,97,45,47,49,50,55,60,80,82,45,47,49,50,55,60,80,82,85,90,95,97]
def building():
    t.width(10)
    global building_height
    global building_width
    for i in range(1):
        height = building_height.pop()

        width = building_width.pop()
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        
# sanjana

def farbuildings():
    global building_gradient
    t.speed(0)
    t.penup()
    t.goto(-400,-250)
    t.pendown()
    t.pensize(1)
    t.setheading(90)
    for row in range(3):
        
        popper = building_line.pop()
        t.color(popper)
        pop = building_gradient.pop()
        t.fillcolor(pop)
        t.begin_fill()

        for b in range(15):
            t.setheading(90)
            building()
            
        t.end_fill()
        t.penup()
        t.goto(-400, t.ycor() - 70) 
        t.pendown()
        t.setheading(90)
def wave():
    t.penup()
    t.goto(600, -300)  
    t.pendown()
    
    for w in range(5):
        t.pencolor("steelblue")
        t.fillcolor("darkblue")
        t.begin_fill()
        for splash in range(10):
            t.circle(50, 180)  
            t.left(180) 
            t.penup()
            t.pendown()
        t.end_fill()
        t.penup()
        t.goto(600, t.ycor() - 20) 
        t.pendown()

wavesplease = input("Would you like the cityscape to be behind an ocean?")
y = ["yes","y","Y","YES","Yes"]
if wavesplease in y:
    farbuildings()
    wave()
else:
    farbuildings()



trtl.speed(0)
trtl.done()