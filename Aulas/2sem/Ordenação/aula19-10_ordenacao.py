'''
lista = [4,2,5,7,3,1,0]
ordenada = []

lista = [4,2,5,7,3,1]
ordenada = [0]

lista = [4,2,5,7,3]
ordenada = [0,1]

lista = [4,5,7,3]
ordenada = [0,1,2]

lista = [4,5,7]
ordenada = [0,1,2,3]

lista = [5,7]
ordenada = [0,1,2,3,4]

lista = [7]
ordenada = [0,1,2,3,4,5]

lista = []
ordenada = [0,1,2,3,4,5,7]

ordenada = []
print(lista)
print(ordenada)
print()
for i in range(len(lista)):
    indice = acha_menor(lista)
    menor = lista.pop(indice)
    ordenada.append(menor)
    print(lista)
    print(ordenada)
    print()

'''

def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato < menor:
            menor = candidato
            indice_menor = i
    return indice_menor

def ordena_bem_ruim(lista):
    ordenada = []
    while lista:
        indice = acha_menor(lista)
        menor = lista.pop(indice)
        ordenada.append(menor)
    return ordenada
def ordena_ruim(lista):
    for i in range(len(lista)):
        indice_delay = acha_menor(lista[i:])
        indice = indice_delay + i
        aux = lista[i]
        lista[i] = lista[indice]
        lista[indice] = aux
    return lista

lista = [4,2,5,7,3,1,0]
#crie um algoritmo que printe elementos vizinhos da lista atÃ© o fim dela (rolling window tamanho 2)
#->4 2
#->2 5
#->5 7
#->7 3
#->3 1
#->1 0
#crie um algoritmo que troque elementos vizinhos da lista atÃ© o fim dela
def bubble_sort(lista):
    for j in range(len(lista)):
        trocas = 0
        for i in range(len(lista)-1-j):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                trocas += 1
        if trocas == 0:
            break
    return lista
import random
from time import time
aleatorios = [random.randint(0,100) for i in range(100000)]
t1 = time()
ordena_bem_ruim(aleatorios)
t2 = time()
print(t2-t1)
aleatorios = [random.randint(0,100) for i in range(100000)]
t1 = time()
bubble_sort(aleatorios)
t2 = time()
print(t2-t1)
