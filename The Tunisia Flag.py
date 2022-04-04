import turtle as t

def square():
    for i in range(4):
        t.forward(540)
        t.right(90)

def triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

def star():
    for i in range(5):
        t.forward(160)
        t.right(144)

t.reset()
t.speed(0)

t.penup()
t.goto(-300, 270)
t.pendown()
t.color("red")
t.begin_fill()
square()
t.end_fill()

t.penup()
t.goto(120, 0)
t.pendown()

t.color("white")
t.begin_fill()
t.left(90)

t.circle(200)
t.end_fill()

t.penup()
t.goto(100, 0)
t.pendown()

t.color("red")
t.begin_fill()

t.circle(180)
t.end_fill()
t.color("white")
t.seth(90)
t.begin_fill()
t.circle(150)
t.end_fill()

t.color("red")
t.penup()
t.goto(-70, -70)
t.pendown()
t.begin_fill()
star()
t.end_fill()

t.penup()
t.goto(-30, -250)
t.pendown()
t.color("white")
t.write("The Tunisa Flag", font=("Arial", 24, "normal"))
t.penup()
t.pen(shown=False, pendown=False, pensize=10)
screen = t.Screen()
screen.exitonclick()
