import os
os.system('cls')

#Crie uma coleção de dados(lista,tupla,dicionário) e
#trabalhe com a função enumerate Aplicando condicionais

lista_nomes = ['Pedro' , 'Tiago' , 'Marcos' , 'Jose']

tupla_frutas = ('abacaxi' , 'morango' , 'manga' , 'banana')

#dic_estados = ['SC':'Santa Catarina' , 'PR':'Parana' , 'RS':'Rio Grande do Sul']

print(list(enumerate(lista_nomes)))

for i , valor in enumerate(lista_nomes):
    if i > 1:
        break
    else:
        print(valor)



