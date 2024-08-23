nome = 'Pedro'

idade = 30

print('O seu nome é' , nome, 'e sua idade é', idade)
print('O seu nome é ' +nome + ' e sua idade é ' +str(idade))
print('O seu nome é {} e sua idade é {} ' .format(nome, idade))
print(f'O seu nome é {nome} e sua idade é {idade}')


altura = 1.238638956
peso = 36.9307450367

print('Sua altura é {:.2f} e seu peso é {:.1f} '.format(altura, peso))
print('Sua altura é {} e seu peso é {} '.format(round(altura), round(peso)))
print(f'Sua altura é {altura:.2f} e seu peso é {peso:.1f} ')
