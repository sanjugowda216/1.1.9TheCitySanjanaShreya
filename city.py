import turtle
import random
t = turtle.Turtle()
building_height = [150,160,170,175,180,190,200,210,230,350,390,400]
building_width = [45,47,49,50,55,60,80,85,90,95,97,100]
# sanjana
def building():
    global building_height
    global building_width
    for i in range(1):
        height = random.choice(building_height)
        building_height.remove(height)

        width = random.choice(building_width)
        building_width.remove(width)

        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        
# sanjana
def farbuildings():
    t.penup()
    t.goto(-400,-100)
    t.pendown()
    t.setheading(90)

    t.fillcolor("black")
    t.begin_fill()

    for b in range(11):
        t.setheading(90)
        building()
        
    t.end_fill()

farbuildings()
turtle.speed(0)
turtle.done()
