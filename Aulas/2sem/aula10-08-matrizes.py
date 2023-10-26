def imprime_elemento_matriz(matriz):
    for linha in range(len(matriz)):
        print(f"Prints da {linha+1}ª linha")
        for coluna in range(len(matriz[0])):
            print(matriz[linha][coluna])
    return
# def imprimi_matriz(matriz):

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]

# for linha in range(len(matriz1)):
#     for coluna in range(len(matriz1)):
#         matriz1[linha][coluna]=0
# imprimi_elemento_matriz(matriz1)

# for i in range(len(matriz1)):
#     for j in range(len(matriz1[0])):
#         if j==i:
#             matriz1[i][j]=1
#         else:
#             matriz1[i][j]=0
# imprimiMatriz(matriz1)

# for linha in range(len(matriz1)):
#     colunas_pares=[]
#     for coluna in range(len(matriz1)):
#         if coluna%2==0:
#             colunas_pares.append(matriz1[linha][coluna])
#     print(f"coluna par : {colunas_pares}")

'''
#printe somente as colunas pares da matriz
#printe somente as linhas impares da matriz
#printe somente a diagonal da matriz
'''
print("---------------------\nColunas Pares\n---------------------")
for coluna in range(0,len(matriz1[0]),2):
    print(f"coluna:{coluna}")
    for linha in range(len(matriz1)):
        print(matriz1[linha][coluna])

print("---------------------\nLinhas Impares\n---------------------")
for i in range(1,len(matriz1),2):
    print(f"Linha:{i}")
    for j in range(len(matriz1[0])):
        print(matriz1[i][j],end=' ')
    print("\n")

print("---------------------\nDiagonal Principal\n---------------------")
for linha in range(len(matriz1)):
    print(" "*2*linha, end='')
    print(matriz1[linha][linha])

print("------------------------")

'''
#defina uma função que recebe dois parametros: nº de linhas e colunas.
#esta função deve criar uma matriz somente com elementos zero e devolvê-la como retorno
'''

def criar_matriz(linhas,colunas):
    ''''
    Jeito Matheus

    # matriz=[]
    # for linha in range(len(linhas)):
    #     linhas_da_matriz=[]
    #     for coluna in range(len(colunas)):
    #         linhas_da_matriz.append(colunas)
    # matriz.append(linhas)
    '''

    matriz=[]
    for i in range(linhas):
        matriz.append([])
        # print(matriz)
        for j in range(colunas):
            matriz[i].append(0)
        # print(matriz)
    return

identidade = criar_matriz(3,3)
identidade2 = criar_matriz(3,3)

#crie uma função que recebe duas matrizes de mesma dimensão e retorna a soma delas

def soma_matriz(m1,m2):
    linhas = len(m1)
    colunas = len(m2)
    if linhas == len(m2) and colunas == len(m2[0]):
        soma = criar_matriz(linhas,colunas)
        for i in range(linhas):
            for j in range(colunas):
                soma[i][j] = m1[i][j]+m2[i][j]
        return soma
    else :
        print(f"Não é possivel somar matrizes de dimensões distintas!")
# matriz_criada1 = criar_matriz(3,4)
# print(matriz_criada1)
# matriz_criada2 = criar_matriz(4,4)
# print(matriz_criada2)
# print("\n")
# soma12 = soma_matriz(matriz_criada1,matriz_criada2)
# if soma12:
#     print(soma12)


# escreva uma função que recebe uma matriz e retorna a sua transposta
def transposta(matriz):
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])//2):
                aux = matriz[i][j]
                matriz[i][j] = matriz[j][i]
                matriz[j][i] = aux
    return matriz
matriz01 = [[1,2,3],[4,5,6],[7,8,9]]
matriz01 = transposta(matriz01)
print(matriz01)



