############        modulo do programa
def soma(x,y):
    return x + y

#####função que retorna valor maximo de uma lista

def calcula_maximo(x,y,z):
    lista = [x,y,z]
    print(max(lista))

def chama_input():
    cidade = input("Digite a cidade: ")
    print(cidade)

###########         funções que só rodam se o programa for rodado de forma direta
###########     não esta acessivel para importação para outros programas python

####        metodo magico   "__main__"

if __name__ == "__main__":
    print(soma(2,3))
    print("Executei sozinho")

    var1 = "João"






