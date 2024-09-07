'''Exercício 5: Escreva um programa que jogue "pedra, papel ou tesoura" 
contra o usuário. O jogo deve continuar até o usuário escolher parar,
e retornar o número de vitórias do usuário, da máquina, e empates.'''


import random

vitorias_usuario = 0
vitorias_maquina = 0
empates = 0

while True:
    print("  ######## Jogo Pedra, Papel ou Tesoura ######")
    print("  #             1. Pedra                     #")
    print("  #             2. Papel                     #")
    print("  #           3. Tesoura                     #")
    print("  #            4. Parar                      #")
    print("  ############################################")
    
    escolha = input("Digite sua escolha (1-4): ")
    
    if escolha == '4':
        break
    
    escolhas = {'1': 'Pedra', '2': 'Papel', '3': 'Tesoura'}
    
    if escolha not in escolhas:
        print("Opção inválida! Tente novamente.")
        continue
    
    usuario = escolhas[escolha]
    maquina = random.choice(['Pedra', 'Papel', 'Tesoura'])
    
    print(f"\nVocê escolheu: {usuario}")
    print(f"A máquina escolheu: {maquina}")
    
    if usuario == maquina:
        resultado = "Empate"
    elif (usuario == 'Pedra' and maquina == 'Tesoura') or \
         (usuario == 'Papel' and maquina == 'Pedra') or \
         (usuario == 'Tesoura' and maquina == 'Papel'):
        resultado = "Vitória"
    else:
        resultado = "Derrota"
    
    print(f"Resultado: {resultado}\n")
    
    if resultado == "Vitória":
        vitorias_usuario += 1
    elif resultado == "Derrota":
        vitorias_maquina += 1
    else:
        empates += 1

print("=== Resultados Finais ===")
print(f"Vitórias do Usuário: {vitorias_usuario}")
print(f"Vitórias da Máquina: {vitorias_maquina}")
print(f"Empates: {empates}")
print("=========================")
