from circulo import Circulo
from quadrado import Quadrado

while True:
    print("\nEscolha uma forma para desenhar:")
    print("1 - Círculo")
    print("2 - Quadrado")
    print("0 - Sair")
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == '1':
        forma = Circulo()
        forma.desenhar()
    elif escolha == '2':
        forma = Quadrado()
        forma.desenhar()
    elif escolha == '0':
        print("Saindo do programa")
        break
    else:
        print("Opção inválida :( ")
