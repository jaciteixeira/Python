
'''
resposta = input("Bem vindo a calculadora! Você gostaria de conhece-lá? (s/n):")
while resposta != "s" and resposta !="n":
    resposta = input("Você gostaria de conhece-lá? (s/n):")
if resposta == "n":
    print("TCHAU!")

else:
    while True:
        opcao = input("\nsoma (+)\nsubtração (-)\nmultiplicação (*)\ndivisão (/)\nsair (sair)"
                         "\nDigite a operação  que você gostaria de tentar :")
        while opcao != "+" and opcao != "-" and opcao != "*" and opcao != "/" and opcao!="sair":
            opcao = input("digte uma das opções a cima: ")

        if opcao == "sair":
            print("\nVALEU!")
            break

        num1 = input("digite um numero:")
        while not num1.isnumeric():
            num1 = input("deve ser um numero")
        num2 = input("digte outro numero: ")
        while not num2.isnumeric():
            num2 = input("deve ser um numero")
        num1=int(num1)
        num2=int(num2)

        if opcao == "+":
            print(f"\n{num1} {opcao} {num2} é igual a: {num1 + num2} ")
        elif opcao == "-":
            print(f"\n{num1} {opcao} {num2} é igual a: {num1 - num2} ")
        elif opcao == "*":
            print(f"\n{num1} {opcao} {num2} é igual a: {num1 * num2} ")
        elif opcao == "/":
            print(f"\n{num1} {opcao} {num2} é igual a: {num1 / num2} ")

'''

# lista_pares = [2,4,6,8,10]
# for num in lista_pares:
#     print(num)

'''
lista_prof=["Alexandre","Danilo","Rita","Erick","João","Allen"]
i=0
for prof in lista_prof :
    if prof =="Danilo":
        print(f"{prof} é o melhor professor de todos!")
    elif prof == "Allen":
        print(f"{prof} é forgado")
    # if prof == "Rita":
    #     print(f"{prof} esta na {lista_prof.index(prof)+1}ª posição")
    else:
        print(f"{prof} é legal")

#     if prof == "Rita":
#         indice_da_rita = i
#     i+=1
#
# print(indice_da_rita)
# print(lista_prof[indice_da_rita])

novos_profs = int(input("digite quantos profs: "))
for prof in range(novos_profs):
    nome = input("Digite o nome: ")
    lista_prof.append(nome)
print(lista_prof)
print(f"há {len(lista_prof)} professores no total")
frase =f"Agora os  "
for nome in lista_prof:
    frase += f"{nome}"
frase += f"são professores"
print()
'''


# list_num = [1,2,6,8,15,64,69,3,68,22,21,54,78,0]
# pares=0
# impares=0
# soma=0
# """
# # for num in range(len(list_num)):
# #     if list_num[num]%2==0:
# #         pares+=1
# #     else:
# #         impares += 1
# """
# for num in list_num:
#     if num%2==0:
#         pares+=1
#     else:
#         impares+=1
#     soma +=num
#     media=soma/len(list_num)
#     # print(soma)
# print(f"total pares: {pares}")
# print(f"total impares: {impares}")
# print(f"Soma: {soma}")
# print(f"Media: {media:.2f}")

'''
lista_prof=["Alexandre","Danilo","Rita","Erick","João","Allen"]
novos_profs = int(input("digite quantos profs: "))
for prof in range(novos_profs):
    nome = input("Digite o nome: ")
    lista_prof.append(nome)
print(lista_prof)
print(f"há {len(lista_prof)} professores no total")
'''
