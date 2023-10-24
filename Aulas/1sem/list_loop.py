# t = 9
# valor = 0
# while t <17:
#     print(f"o valor é {valor} e o tempo é {t}")
#     if t<=12 and t<14:
#         t+=1
#         continue
#     valor +=100
#     t+=1
# print(f"o valor é {valor} e o tempo é {t}")


# nota = float(input("Digite a nota: "))
# contagem = 1
# while nota < 0 or nota >10:
#     nota = float(input(f"Digite uma nota entre 0 e 10: "))
#     contagem +=1
#     if contagem >2:
#         print("voce errou 3x!")
#         break
# if contagem <3:
#     print(f"você acertou, nota digitada: {nota}")


'''
nome = input("digite o nome: ")
while len(nome) < 3:
    nome = input("digite um nome com mais de 3 letras: ")

idade = input("digite a idade:")
if idade.isnumeric():
    if int(idade)> 0 and int(idade)<150:
        print("digitou corretamente!")
    # elif  int(idade)< 0 or int(idade)>150:
    #     idade = input("digite uma idade entre 0 e 150:")
else:
    while True:
        idade = input("dever se um numero: ")
        if idade.isnumeric():
            idade_convertida = int(idade)
            if idade_convertida <0 or idade_convertida > 150:
                print("digite uma idade entre 0 e 150:")
                continue
            else:
                print("digitou certo!")
                break

while idade < 0 or idade>150:
    idade = int(input("digite uma idade entre 0 e 150: "))

salario = float(input("Digite o salario: "))
while salario <=0:
    salario = float(input("Digite o valor maior que 0: "))

sexo = input("digite o gerero, F=feminino ou M=masculino: ")
while sexo != "f" and sexo!= "m":
    sexo = input("digite f ou m: ")
if sexo == "f":
    sexo = "feminino"
elif sexo == "m":
    sexo = "masculino"

estado_civil = input("c=casado\n "
                     "s=solteiro\n "
                     "d=divorciado\n"
                     "v=viuvo\n"
                     "digite o estado civil:")
while estado_civil != "c" and estado_civil != "s" and estado_civil != "d" and estado_civil != "v":
    estado_civil = input("digite novamente:")

print(f"nome: {nome}\nidade:{idade}\ngenero:{sexo}\n estado civil:{estado_civil}")
'''

a= 80000
b=200000
t=0
while a<b:
    a*=1.03
    b*=1.015
    t+=1
print(f"apos {t} anos a passou b com populaçao {a:.2f}")



