

# indice = 0
# lista = [1,625,65,2541,15,565,515,15,36,54,100,326]
# for num in lista:
#     if num==100:
#         indice_100 = indice
#     indice+=1
#     print(f"O numero 100 está na posição {indice_100}")


"""
#crie uma lista com 10 números
#conte a quantidade de numeros pares e a quantidade de numeros impares na lista
numeros = [1,625,65,2541,15,565,515,15,36,54]
pares=0
impares=0
for numero in numeros:
    if numero%2==0:
        pares+=1
    else:
        impares+=1
print(f"PARES: {pares}")
print(f"IMPARES: {impares}")
"""

# # crie uma lista vazia
# # pergunte ao usuário quantos nomes ele quer cadastrar
# # cadastre, ou seja use o append
# # e verifique se o danilo está na lista
# # caso esteja, printe que eu sou professor.
# indice = 0
# qtd_nomes = input("Digite a quantidade: ")
# while not qtd_nomes.isnumeric():
#     qtd_nomes = input("tem que ser um numero: ")
# qtd_nomes = int(qtd_nomes)
#
# lista = []
# # ta_ou_nao = False
# for nome in range(qtd_nomes):
#     nome = input(f"digite o  nome: ")
#     lista.append(nome)
#     # if nome=="danilo":
#     #     ta_ou_nao = True
#     #     print(f"{nome} é professor")
#
# # if ta_ou_nao:
# #     print(f"danillo ta na lista")
# # else:
# #     print(f"ele não tá!")
#
# if "danilo" in lista:
#     print(f"{nome} é professor")
# else:
#     print(f"{nome}")
#
# print(lista)

def verifica_par(numero):
    if numero%2==0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")

qtd = int(input("digite a qtd: "))
for i in range(qtd):
    num = int(input("digite um numero: "))
    verifica_par(num)

lista_numeros = [1,62,65,254,15,5658,515,15,36,54]
for num in lista_numeros:
    verifica_par(num)