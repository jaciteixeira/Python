def par_ou_impar(numero):
    pares =0
    impares=1
    for num in numero:
        if num%2 == 0:
            pares+=1
        else:
            impares+=1
        return [pares,impares]
    # if numero%2 ==0:
    #     return f"O {numero} é par"
    # else:
    #     return f"O {numero} é impar"

def retorna_indice_maior(lista):
    maior = lista[0]
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
    return indice_maior

# def retorna_indice_menor(lista):
#     indice_menor=0
#     for i in range(len(lista)):
#         print(f"testar se lista[{i}] ou seja {lista[i]}>{menor}")
#         if lista[i]<lista[indice_menor]:
#             print(f" O maior valia {menor} no indice {indice_menor}")
#             menor=lista[i]
#             indice_menor = [i]
#             print(f"o maior passa a valer {menor} no indice {indice_menor}")
#     return indice_menor

def cadrastra_vinho(vinhos,qtd):
    for i in range(qtd):
        nome = input("diga o nome: ")
        vinhos.append(nome)
    return vinhos

def cadrastra_preco(precos,qtd):
    for i in range(qtd):
        nome = input("diga o preco: ")
        precos.append(nome)
    return precos


def verificar_numero(frase):
    print("cai na função verificar")
    num = input(frase)
    while not num.isnumeric():
        print("digite um numero: ")
        num = input(frase)
    return int(num)
def soma_lista(numeros):
    soma = 0
    for num in numeros:
        soma+=num
    return soma

def media(numeros):
    soma = soma_lista(numeros)
    for num in numeros :
        soma+=num
    media =  soma/len(numeros)
    return media

def verificar_opcoes(msg, opcao):
    while not opcao in msg:
        opcao = input(f"Digite uma opção valida!" + msg)
        return opcao

# resultado = par_ou_impar([2,4,8,7,9,12])
# qtd_pares = resultado[0]
# qtd_impares =  resultado[1]
# print(qtd_pares)
# print(qtd_impares)
# # print(par_ou_impar(659544115))
# # print(659549%2)

#faça uma função que recebe uma lista de numeros e retorna o indice do menor numero

lista= []
i=0
vezes = verificar_numero("digite a qtd de vezes: ")
print(f"voltei,vezes = {type(vezes)}")

while i<vezes:
    numeros = verificar_numero(f"digite o numero: ")
    lista.append(numeros)
    print(lista)
    i+=1
print(lista)

# maior = lista_numeros[0]
# for num in lista_numeros:
#     print(f"testar se {num}>{maior}")
#     if num>maior:
#         print(f"trocar {maior} por {num}")
#         maior=num
# print(maior)




# local_maior = retorna_indice_maior(numeros)
# print(numeros[local_maior])
# local_menor = retorna_indice_menor(numeros)
# print(numeros[local_menor])



valor_precos = [20,40,50,15,25,100,10]
nome_vinhos=['rose','tinto','branco','seco','suave','suavinho','licoroso']
print(media(valor_precos))
qtd = verificar_numero("qts vinhos: ")

# local_mais_caro = retorna_indice_maior(valor_precos)
# print(nome_vinhos[local_mais_caro])
# local_mais_barato = retorna_indice_menor(valor_precos)
# print(nome_vinhos[local_mais_barato])

# nome_vinhos = cadrastra_vinho(nome_vinhos,qtd)
# precos = cadrastra_preco(valor_precos,qtd)
# print(nome_vinhos)




