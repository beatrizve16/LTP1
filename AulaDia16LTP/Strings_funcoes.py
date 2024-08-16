
texto = '___linguagens e técnicas de Programação técnicas___'


#imprimir intervalos 𐙚 ᯓ★

print(type(texto)) #imprime o tipo
print(len(texto)) # imprimi o tamamho da string
print(texto[13]) #imprimi uma letra especifica
print(texto[0:12]) #imprimi de uma letra ate outra mas imprimi so ate a anterior -> 0-11
print(texto[:12])#se nao colocar no comeco significa 0
print(texto[:])#do comeco ao fim
print(texto[-10:-5]) #vai de traz para frente


#funções ✧˖°🌷📎⋆ ˚｡⋆୨୧˚

#CAPITALIZAÇÃO ₊˚🖇️✩ ₊˚🎧⊹♡
print(texto.upper()) #maiusculo
print(texto.lower()) #minusculo
print(texto.capitalize()) #coloca a primeira letra maiuscula
print(texto.title()) #coloca toda primeira letra maiuscula
print(texto.swapcase()) #inverte maiuscula -> minuscula / minusxcula-> maiuscula

#REMOVER 🧸🤎🪐
print(texto.strip()) #tira os espacos
print(texto.strip('_')) #tira um caractere especifico SOMENTE do incio e fim
print(texto.rstrip()) #re coloca

#SUBSTITUIR ˙✧˖°📷 ⋆｡˚꩜
print(texto.replace('linguagens','Códigos')) #substitui o qe voce quiser!!!! :D
print(texto.replace('','_'))

#ENCONTRAR 🪐⋆｡°✩
print('técnicas' in texto) #procurar uma string
print(texto.find('e')) #retorna um inteiro= indice da posicao da primeira ocorrencia daquele caractere
print(texto.find('técnicas')) #mostra so o indice do primeiro elemento da palavra (ESQUERDA PARA DIREITA)
print(texto.rfind('técnicas')) #mostra so o indice do primeiro elemento da palavra  (ESQUERDA PARA DIREITA) MAS DO QUE ESTA MAIS PRO FINAL

#SEPARA ˚˖🌷͙֒✧˚.⋆
print(texto.split()) #separa as palavras pelo caractere que esta dentro dos parentesis (normalmente o espaco)
texto2 = texto.split()
print(type(texto2))
print(''.join(texto2))
a=['Hello' , 'World']
print(texto.join(a)) #JUNTA TUDO 


#IDENTIFICA O TIPO
print(texto.isalpha())
print(texto.isalnum())
