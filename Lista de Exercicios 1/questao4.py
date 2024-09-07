'''Exercício 4: Dada uma lista de notas de alunos 
notas = [6.3, 7.5, 9.2, 5.1, 6.8], 
calcule e exiba a média das notas.
Além disso, exiba a quantidade de notas acima da média (6).'''

notas = [6.3, 7.5, 9.2, 5.1, 6.8]

media = sum(notas) / len(notas)

acima_da_media = 0
for nota in notas:
    if nota > media:
        acima_da_media += 1

print("média:", media)
print("notas acima da média:", acima_da_media)
