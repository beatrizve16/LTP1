import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("beige")
t.pensize(5)


t.color("#6B705C", "#B7B7A4")
t.begin_fill()
t.penup()
t.goto(-100, -100)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()


t.color("#6B705C", "#B7B7A4")
t.begin_fill()
t.goto(-100, 100)
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

t.color("#CB997E", "#DDBEA9")
t.begin_fill()
t.penup()
t.goto(15, - 100)
t.pendown()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.end_fill()

t.color("#CB997E", "#DDBEA9")
t.begin_fill()
t.penup()
t.goto(-75, - 20)
t.pendown()
t.forward(50)
t.left(90)
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
t.end_fill()

t.color("#CB997E", "#DDBEA9")
t.penup()
t.goto(-75, - 20)
t.pendown()
t.forward(-40)
t.left(90)
t.forward(50)

t.color("#CB997E", "#DDBEA9")
t.penup()
t.goto(-75, - 20)
t.pendown()
t.forward(25)
t.left(90)
t.forward(70)

t.hideturtle()
turtle.done()
