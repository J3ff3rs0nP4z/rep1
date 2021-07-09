
arqu1 = open('arquivo.txt' , 'r')

print(arqu1.read())




#gerenciador de contexto de arquivos você pode manipular arquivos dentro de um
#bloco de codigo

with open("manipulando.txt", "w+") as f:
    f.write('Teste Linha\n')
    f.write("Teste Linha\n")
    f.seek(0,0)


    grava = str(f.read())

with open('manipulando.txt', 'w+') as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())


    
