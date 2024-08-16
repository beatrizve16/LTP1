import turtle

# Configuração inicial
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

# Desenhando o corpo da casa
t.color("black", "lightblue")  # Contorno preto e preenchimento azul claro
t.begin_fill()
t.penup()
t.goto(-100, -100)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Desenhando o telhado
t.color("black", "brown")  # Contorno preto e preenchimento marrom
t.begin_fill()
t.goto(-100, 100)
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Desenhando a porta
t.color("black", "darkblue")  # Contorno preto e preenchimento azul escuro
t.begin_fill()
t.penup()
t.goto(-30, -100)
t.pendown()
t.goto(-30, 0)
t.goto(30, 0)
t.goto(30, -100)
t.goto(-30, -100)
t.end_fill()

# Desenhando uma janela
t.color("black", "yellow")  # Contorno preto e preenchimento amarelo
t.begin_fill()
t.penup()
t.goto(50, 0)
t.pendown()
for _ in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Finalizando o desenho
t.hideturtle()
turtle.done()
