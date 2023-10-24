'''
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print("\n")
    return

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        #print(matriz)
        for j in range(colunas):
            import random
            matriz[i].append(random.randint(1,5))
        #print(matriz)
    return matriz
def soma_elementos(vetor):
    soma = 0
    for coluna in range(len(vetor[0])):
        soma += vetor[0][coluna]
    print(f"soma dos pesos:{soma}")
    return soma

alunos = 10
pesos = cria_matriz(1,5)
pesos1 = [1,2,3,2,1]
notas = cria_matriz(5,alunos)
mostra_matriz(pesos)
mostra_matriz(notas)
soma_elementos(pesos)
medias = []

for coluna in range(alunos):
    soma_pesos = soma_elementos(pesos)
    soma = 0
    for linha in range(len(pesos1)):
        soma+=pesos[0][linha]*notas[linha][coluna]
        print(f"soma das notas:{soma}")
    media = soma /soma_pesos
    print(media)
    medias.append(media)
print(f"Medias: {medias}")
'''

# dic = {'sao paulo':'sao paulino',
#        'corinthians':'cornthiano',
#        'palmeiras':'palmerense',
#        'santos':'santista',
#        'vasco':'vascaino'}
#
# time = input(f"Que time você torce? ")
#
# while time != 'sair':
#     print(f"Você é um {dic[time]}")
#     time = input(f"digite o time: ")
#     if time != dic.keys() and time != 'sair':
#         print("invalido: ")
#         time = input(f"digite o time: ")
#
# dicChave = {'chave1':'valor1'}
# print(dicChave)
# dicChave['chave2'] = 'valor2'
# for key in dicChave.keys():
#     print(dicChave(key))

'''
dicionary = {}
dicionary['pares']= []
dicionary['impares']= []

for i in range(10):
    if i%2==0:
        dicionary['pares'].append(i)
    else:
        dicionary['impares'].append(i)
print(dicionary)
'''

carros = {'modelo':['j3','celta','palio','uno','hb20'],
          'preco':[120,660,1000,364,92]}

# carros['modelo']=[]
# carros['preco']=[]
# for i in range(2):
#     modelo = input("digite o modelo: ")
#     carros['modelo'].append(modelo)
#     preco = input("digite o preco: ")
#     carros['preco'].append(preco)
# print(carros)

def local_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i]> maior:
            indice_maior = i
            maior = lista[i]
    return indice_maior

mais_caro = local_maior(carros['preco'])
print(f"O carro mais caro é o {carros['modelo'][mais_caro]}")

carros['potencia']=[]
print(carros)

for carro in carros['modelo']:
    potencia = input(f"digite a potencia do {carro}: ")
    carros['potencia'].append(potencia)
print(carros)





