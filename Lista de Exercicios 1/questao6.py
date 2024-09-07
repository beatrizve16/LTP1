'''Exercício 6: Crie um programa que gerencie o banco de dados de uma biblioteca.
O programa deve permitir adicionar um novo livro (como uma lista contendo título, 
autor e ano), listar todos os livros, e permitir a busca de livros pelo título.'''

biblioteca = []

while True:
    print("=" * 31)
    print("|| Gerenciador de Biblioteca ||")
    print("=" * 31)
    print("1. Adicionar novo livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro por título")
    print("4. Sair")
    print("=" * 30)
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == '1':
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")
        livro = [titulo, autor, ano]
        biblioteca.append(livro)
        print("Livro adicionado com sucesso!\n")
        
    elif opcao == '2':
        print("=" * 30)
        print("    Lista de Livros")
        print("=" * 30)
        if biblioteca:
            for livro in biblioteca:
                print(f"Título: {livro[0]}")
                print(f"Autor: {livro[1]}")
                print(f"Ano: {livro[2]}")
                print("-" * 30)
        else:
            print("Nenhum livro cadastrado.\n")
    
    elif opcao == '3':
        busca_titulo = input("Digite o título do livro para busca: ")
        encontrado = False
        print("=" * 30)
        print("    Resultados da Busca")
        print("=" * 30)
        for livro in biblioteca:
            if livro[0].lower() == busca_titulo.lower():
                print(f"Título:{livro[0]}")
                print(f"Autor:{livro[1]}")
                print(f"Ano:{livro[2]}")
                print("-" * 30)
                encontrado = True
        if not encontrado:
            print("Livro não encontrado.\n")
    
    elif opcao == '4':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.\n")
