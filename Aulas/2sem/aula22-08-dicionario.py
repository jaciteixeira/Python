import pandas as pd

def garantir_resposta(lista_respostas,msg):
    resposta = input(msg)
    while not pergunta in lista_respostas:
        resposta = input(msg)
    return resposta

def acha_maior(lista):
    indice_maior = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

# carros = {'modelos':['up','ka','celta','gol'],'preço':[10,20,1000,50]}
# carros = pd.DataFrame(carros)
# # print(carros)
# local_mais_caro = acha_maior(carros['preço'])
# print(f"O carro mais caro é o {carros['modelos'][local_mais_caro]} e vale R${carros['preço'][local_mais_caro]}")

#crie uma nova chave potencia e associe a uma lista de valores numericos
#traga todas informações sobre o carro mais potente

# carros['potencia']=[10,20,500,100]
# local_mais_potente = acha_maior(carros['potencia'])

# print(f"O carro mais caro é o {carros['modelos'][local_mais_caro]} "
#       f"e vale R${carros['preço'][local_mais_caro]} "
#       f"e tem potencia {carros['potencia'][local_mais_potente]}")

# print(f"As informações pedidas são: ")

# for key in carros.keys():
#     print(f"{key}: {carros[key][local_mais_potente]}")

#pergunte ao usuario se ele gostaria de cadastrar mais um carro
#se sim, peça as informações referentes a cada chave e as adicione
#se não, encere

# print(carros)
#
#
# while True:
#     pergunta = input(f"deseja cadastra outro carro? [s ou n]: ")
#     if pergunta == 's':
#         print("Diga as informações: ")
#         for key in carros.keys():
#             info = input(f"{key}: ")
#             carros[key].append(info)
#         pergunta = input(f"deseja cadastra outro carro? [s ou n]: ")
#     else:
#         print("cadastro finalizado")
#         print(pd.DataFrame(carros))
#         break

'''
carros_tecnico = {'modelos':['up','ka','celta','gol'],
        'preço':[10,20,1000,50],
        'potencia':[10,20,500,100]
         }
carros_conforto = {
    'modelos':['up','ka','celta','gol'],
    'n° portas': [2,2,4,2],
    'ar condicionado':['n','n','s','n']
}
#una esses dois dicionarios em um só, agora com 5 colunas sem repetição
uniao_carros = {}
print(uniao_carros)
for key in carros_tecnico.keys():
    uniao_carros[key] = carros_tecnico[key]
    print(uniao_carros)
for key in carros_conforto.keys():
    if key not in uniao_carros:
        uniao_carros[key] = carros_conforto[key]
    print(uniao_carros)
print(pd.DataFrame(uniao_carros))
'''

frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
frase = frase.lower().replace('.','').split(' ')
# print(frase)

# criar um dicionario com as palavras da frase
palavras = {}
# for palavra in frase:
#     palavras[palavra] = 0
# print(palavras)
# for key in palavras.keys():
#     for palavra in frase:
#         if palavra == key:
#             palavras[palavra]+=1
# print(palavras)
dic = {}
for palavra in frase:
    if palavra not in dic.keys():
        dic[palavra] = 1
    else:
        dic[palavra] += 1
    print(dic)