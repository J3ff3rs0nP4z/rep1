import os
os.system('cls')


import csv

with open ('nomes.csv', 'w+', newline="") as fcsv:
    escrever = csv.writer(fcsv,delimiter=',')
    escrever.writerow(("Nome" , "Sobrenome" , "Idade"))
    escrever.writerow(("João" , "Ricardo" , 35))
    escrever.writerow(("Juca" , "Souza" , 23))
    escrever.writerow(("Alberto" , "Cunha" , 54))

"""
with open('nomes.csv', 'r') as fcsv:
    ler = csv.reader(fcsv)

#### TRANSFORMANDO O CSV EM ESTRUTURA DE DADOS LISTA

    lista1 = list(ler)
    print(lista1)


for csv in lista1:
    print(csv)

    fcsv.close()
"""

####    TRANSFORMAR O CSV EM DICIONARIO

with open('nomes.csv' , 'r') as fcsv2:
    ler_dict = csv.DictReader(fcsv2)

    #for dic in ler_dict:
    #    print(dic)

    for dic in ler_dict:
        print(dic['Nome'])

    fcsv2.close()



with open("arquivo1.csv" , 'r') as arqu1:
    arqu1 = csv.reader(arqu1)

    ####        iterar os valores do CSV

    #for l in arqu1:
    #    print(l)


    lista2 = list(arqu1)




