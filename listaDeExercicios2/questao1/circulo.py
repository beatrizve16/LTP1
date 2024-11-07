import turtle
from forma import Forma

class Circulo(Forma):
    def desenhar(self):
        t = turtle.Turtle()
        t.circle(50)
        turtle.done()
