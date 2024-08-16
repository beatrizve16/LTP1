import time

texto = 'jas bnbf;ksa djkfsd nkmb'

for letra in texto:
    if letra == ' ':
        print('ESPACO')

# ( inicio (inclusivo), fim (exclusivo), de quanto em quanto)
for i in range(5): #recebe ate tres argumentos
    print('Hello', i)

for i in range(1,6): #recebe ate tres argumentos
    print('Hello', i)

for i in range(-5, 5):
    print('Hello', i)

for i in range(2, 11, 2): #de dois em dois
    print('Hello', i)

for i in range(10, 0, -1): #de traz pra frente
    print('Hello', i)

#funcao sleep -> trava a execucao -> pra demorar
import time
for i in range(2, 11, 2): #de dois em dois
    print('Hello', i)
    time.sleep(1)

