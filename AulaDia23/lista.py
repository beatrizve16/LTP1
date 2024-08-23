from AULADEHOJE import idade

semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')

#semana = ('domingo',30, 'segunda',False, 'terca',3.14, 'quarta')

#semana = 'domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado'


print(semana)
print(len(semana)) #tamanho da lista
print(semana[4]) #imprimi so aquele desse indice
print(len(semana[4])) # imprimi o tamanho do que ta no indice
print(semana.index('quarta')) # imprime o indice da primeira vez que isso aparece
print(semana.count('quarta')) # imprime quantas vezes aparece

print('########################')
idades = (21, 84, 53, 12, 90, 1)
print(max(idades))
print(min(idades))
print(sum(idades))
print(sum(idades)/len(idades))
media = sum(idades)/len(idades)
print(media)

#lista
print('########################')

precos = [10, 11, 12 , 13]


print(precos)
print(precos[-3])
print(len(precos))
print(min(precos))
print(max(precos))
print(sum(precos))
print(sum(precos)/len(precos))
print(precos.index(12))
print(precos.count(11))

print('########################')

precos.append(22.64)
print(precos)

print('########################')

precos.extend([56.45, 72.5])
print(precos)

print('########################')

precos.remove(13)
print(precos)


