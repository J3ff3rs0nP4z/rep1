import json
import urllib.request   #    request de requisição

##   JSON é um formato para troca de dados via internet ou via web
#via http ou htps chama-se JAVASCRIPT OBJECT NOTATIONS


cadastro_pessoas = {
    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}

##  iterar o dicionario

for c,v in cadastro_pessoas.items():
    print(c,v)


    ###     converter dicionarios em arquivos JSON
        #   do modulo vamos usar o json.dump


dados = json.dumps(cadastro_pessoas, indent=4)
print(dados)


##          para salvar o arquivo convertido vamos usar o gerenciador de contexto de arquivo
        ##  dumps trasforma
        ##  dump joga em um arquivo

with open('cadastro_pessoas2.json' , 'w+') as j:
    json.dump(cadastro_pessoas,j,indent=4)



    ####  ler aquivo json para dicionario com a função json.loads

with open('cadastro_pessoas2.json', 'r') as f2:
    le_json = json.load(f2)

    print(le_json)


    for v in le_json.values():
        print(v)


####    importar um json da internet e gravar num arquivo

### WEBSCRAPING   entrar em um site e pegar dados
# para fazer vamos usar urllib

url = 'https://www.sba.gov/sites/default/files/data.json'

##      capturar dados do json

pega_json = urllib.request.urlopen(url).read().decode()


##  converter esses dados em dicionario.  json.loads


dic_json = json.loads(pega_json)

#print(dic_json)

for c in dic_json.values():
    print(c)

##   criaar o arquivo json com o conteudo da internet 

with open('sba.json' , 'w+') as file:
    json.dump(dic_json,file,indent=4)




