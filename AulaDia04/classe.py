class Autor:
    def __init__(self, nome, pais, nascimento):
        self.nome = nome
        self.pais = pais
        self.nascimento = nascimento

    def autorInfo(self):
        print(f'Autor: {self.nome},'
              f'Pais: {self.pais},'
              f'Ano de Nascimento: {self.nascimento}')


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def livroInfo(self):
        print(f'Titulo: {self.titulo},'
              f'ano: {self.ano},'
              f'Autor: {self.autor.nome}')


autor1=Autor('R.F Kuang', 'China', 1996)
livro1=Livro('Yellowface', 2023, autor1)

livro1.livroInfo()
livro1.autor.autorInfo()
