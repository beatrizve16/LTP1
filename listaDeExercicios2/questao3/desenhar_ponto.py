import turtle

def desenhar_ponto(ponto):
    t = turtle.Turtle()
    t.penup()
    t.goto(ponto.x, ponto.y)
    t.pendown()
    t.dot(5)
    turtle.done()
