class Carro(): #metodo contrutor
    def __init__(self, marca, modelo, cor, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.quilometragem = quilometragem

    def acelerar(self):
        print('Vroom!')

    def frenar(self):
        print('carro parando!')


    def getModelo(self):
        return self.modelo

    def setCor(self, novaCor):
        self.cor = novaCor

    def getCor(self):
        return self.cor
