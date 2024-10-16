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
    t.pensize(0)
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
        t.goto(-400, t.ycor() - 50) 
        t.pendown()
        t.setheading(90)

farbuildings()
turtle.speed(0)
turtle.done()
