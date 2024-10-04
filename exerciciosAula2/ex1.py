

class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    def getTitulo(self):
        return self.__titulo
    def getAutor(self, novoTitulo):
        self.__autor = novoTitulo

    @property
    def autor(self):
        return self.__autor

    @property
    def ano(self, novoAno):
        self.__ano = novoAno

livro1=Livro('Yellowface', 2023, 'R.F. Kuang')

print(livro1.getTitulo())
print(livro1.autor)
livro1.ano=2024
