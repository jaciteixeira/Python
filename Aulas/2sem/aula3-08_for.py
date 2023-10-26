'''
num = int(input("diga um numero: "))
if num > 10:
    print(f"O {num} é maior que 10!")
elif num < 10:
    print(f"O{num} é menor que 10!")
else:
    print(f"Voce digitou o 10!")
'''

# senha = "123456"
# input_usuario = input("diga a senha")
# tentativas = 1
# while (not input_usuario == "123456") and tentativas < 3:
#     input_usuario= input("diga a senha: ")
#     tentativas += 1
# if tentativas < 3:
#     print("você acertou!")
# else:
#     print("Sai hacker")

'''
lista = ["danilo","luis","matheus","renata"]
for i in range(len(lista)):
    if lista[i]=="luis":
        print(f"O {lista[i]} está no indice {i}, ou seja, posição {i+1}")
    # print(f"lista[{i}]= {lista[i]}")
'''

#Peça ao usuário 10 numeros e indique a soma dos numeros que ele digitou
#Calcule a média dos números que ele digitou


# cont=0
# soma=0
# while cont < 10:
#     num = int(input("digite um numero: "))
#     cont+=1
#     soma += num
# print(f"Soma={soma} \n"
#       f"Media={soma/cont}")

'''
#COM FOR
soma = 0
for i in range(5):
    num = int(input("digite numero: "))
    soma+=num
print(f"Soma={soma} \n"
      f"Media={soma/(i+1)}")
'''

#Peça ao usuário 10 numeros e os coloque em uma lista
#Calcule a soma dos números que ele digitou
#calcule a media dos numeros que ele digitou

# lista = []
# cont=0
# while cont < 10:
#     num = int(input("digite numero: "))
#     lista.append(num)
#     cont+=1
# print(lista)
#
# soma =0
# for num in lista:
#     soma += num
# print(f"Soma={soma} \n"
#       f"Media={soma/len(lista)}")

lista1 = [1,6,8,92,65,2,6,4,5,12]
lista2 = [6,3,9,8,4,12,52,7,9,33]
#
# iguais=[]
# # for num1 in lista1:
# #     for num2 in lista2:
# #         # print(f"{num1}=={num2}")
# #         if num1 == num2:
# #             iguais.append(num2)
# # print(iguais)
#
# for num1 in lista1:
#     if num1 in lista2:
#         iguais.append(num1)
# print(iguais)


#declare uma lista com 10 numeros
#encontre o maior elemento da lista e a posição dele
#transforme isso em uma função que recebe uma lista e retorna o índice do maior

def encontrarMaior(lista2):
    indiceMaior=0
    maior = 0
    for i in range(len(lista2)):
        if lista2[i]>maior:
            maior = lista2[i]
            indiceMaior = i
    return indiceMaior
localMaior = encontrarMaior(lista2)
print(f"Maior numero: \n"
      f"Posição: {localMaior+1}")








