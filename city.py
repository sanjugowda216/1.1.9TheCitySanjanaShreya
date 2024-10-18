import turtle
import random
t = turtle.Turtle()
building_gradient = ['black','gray','darkgray','lightgray']
building_height = [150,160,170,175,180,190,200,210,230,350,390,210,230,350,390,400]
building_width = [45,47,49,50,55,60,80,82,45,47,49,50,55,60,80,82,85,90,95,97]
# sanjana
def building():
    global building_height
    global building_width
    for i in range(1):
        height = random.choice(building_height)

        width = random.choice(building_width)

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
    t.goto(-400,-150)
    t.pendown()
    t.pensize(1)
    t.setheading(90)
    for row in range(4):
        

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
        t.pencolor("blue")
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
if wavesplease =="yes" or "y" or "YES" or "Yes" or "Y":
    farbuildings()
    wave()
else:
    farbuildings()



turtle.speed(0)
turtle.done()