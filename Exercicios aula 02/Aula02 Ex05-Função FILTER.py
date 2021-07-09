import os
os.system('cls')

#Execute um filtro condicional com a função FILTER utilizando uma tupla.

lista_multi = ('faca' , 35 , 'fogo' , 'casa' , 'gelo' , 22)

def validacao(x):
    return x == 35

print(list(filter(validacao, lista_multi)))
