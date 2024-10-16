import turtle
t = turtle.Turtle()


def building():
    for i in range(1):
        t.forward(200)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(200)
        

def farbuildings():
    t.penup()
    t.goto(-400,-50)
    t.pendown()
    t.setheading(90)

    t.fillcolor("black")
    t.begin_fill()

    for b in range(10):
        t.setheading(90)
        building()
        
    t.end_fill()

farbuildings()
turtle.speed(0)
turtle.done()
