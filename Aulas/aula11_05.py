# profs=[]
# print(profs)
# profs.append("allen")
# print(profs)
# profs.append("ale")
# print(profs)
# profs.append("danilo")
# print(profs)
#
# #APEEND COM FOR (RANGE DA QUANTIDADE DIGITADA PELO USUARIO)
# qtd = int(input("Quantos?: "))
# for i in range(qtd):
#     novo_prof = input(f"digite o  nome: ")
#     profs.append(novo_prof)
#     print(profs)
#
#
# #APEEND COM FOR (RANGE DO CONTEUDO DE OUTRA LISTA)
# lista_inutil = ["item1", False, True]
# for I in range(lista_inutil):
#     novo_prof = input(f"digite o  nome: ")
#     profs.append(novo_prof)
#     print(profs)
#
# #APEEND COM WHILE
# i=0
# while i<3:
#     novo_prof = input(f"digite o {i + 1}°  nome: ")
#     profs.append(novo_prof)
#     print(profs)
#     i+=1
'''
carros = ["Fusca","Golf","Celtinha Brabo","Uno com escada","Kombosa de feira"]
precos = [2_000,200_000,1_000_000,3_000_000,500_000]
maior = precos[0]
for i in range(len(precos)):
    if precos[i] > maior:
        maior = precos[i]
        indice_maior = i
    print(f"O maior valor até agora é {maior}")
print(f"O preço mais alto é {maior} e foi encontrado no indice{indice_maior}")
print(f"O carro mais caro é {carros[indice_maior]}")
'''

def printar_oi():
    print("olá")
# printar_oi()
# printar_oi()
# printar_oi()
# printar_oi()


# qtd = checa_numero(input("qtd profs: "))
# # preco = checa_numero(input("digite um numero: "))
# # print(qtd)
# # print(preco)



def checa_numero(a,frase, tentativas):
    # a = input("diga um numero: ")
    i=0
    while not a.isnumeric() and i<tentativas:
        a= input("UM NUMERO! :")
        i+=1
    if i<tentativas:
        a=int(a)
        print(f"{a} é um numero!")
    return a

def par_impar(numero):
    if numero % 2 == 0:
        print(f"O numero {numero} é par!")
    else:
        print(f"{numero} é impar")
    return numero

frase1 = "qts profs: "
qtd_profs = input(frase1)
qtd = checa_numero(qtd_profs,frase1,3)
frase2 = "diga um numero(qtd)"
preco = input(frase2)
preco = checa_numero(preco,frase1,5)

# num = checa_numero(input("digite um numero: ") , frase1,2)
#
num = par_impar(checa_numero(input("digite um numero: ") , frase1,2))
print(qtd_profs,qtd,num)






