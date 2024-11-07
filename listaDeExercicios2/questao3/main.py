from ponto import Ponto
from desenhar_ponto import desenhar_ponto

x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))

ponto = Ponto(x, y)
desenhar_ponto(ponto)
