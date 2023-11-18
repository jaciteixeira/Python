'''lista = [2,4,5,0,1]
j=0
total=0
while True:
    trocas = 0
    for i in range(len(lista)-j-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            trocas +=1
        print(lista)
    j+=1
    total += trocas
    if trocas == 0:
        break
print()
print(total,(len(lista)**2+ len(lista))/2)'''

# Pergunta ao usuário qual número deseja encontrar a raiz quadrada
numero_desejado = float(input("Digite o número do qual você deseja encontrar a raiz quadrada: "))

# Inicializa as variáveis para o cálculo
numero_aproximado = 0
menor_diferenca = abs(numero_desejado)
passo = 0.01

# Gera números entre 0 e o número desejado com um intervalo de 0.01
for numero in range(int(numero_desejado * 100) + 1):
    numero_teste = numero * passo
    diferenca = abs(numero_teste**2 - numero_desejado)

    # Verifica se esta é uma diferença menor
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        numero_aproximado = numero_teste

# Exibe o resultado
print(f"A raiz quadrada aproximada de {numero_desejado} é aproximadamente {numero_aproximado}")
