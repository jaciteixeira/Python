lista = [4,2,1,7,6,3,0,9,8,5]

"""faça um for que printe elementos vizinhos"""
'''reutilize o for do exercicio anterior para trocar elementos vizinhos
repita até a lista estar ordenada'''

print(f'lista sem ordenação: {lista}')
# lista.sort()
# print(lista)
while True:
    trocas = 0
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            trocas +=1
            # print(f'indice:{i} elemento{i+1}:{lista[i+1]} ')
            print(f'{lista}')
    if trocas ==0 :
        break

passo = 0.01
inicio = 0
num = 10
lista = []
while inicio<=num:
    lista.append(inicio)
    inicio+=passo
raiz = 0
for i in range(len(lista)):
    candidato = lista[i]
    if abs((candidato**2)-num)< abs((raiz**2)-num):
        raiz = candidato
print(raiz)
