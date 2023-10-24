"""
num = int(input("Diga um numero: "))

resto = num%3

if resto == 0:
    print("é divisivel")
else:
    print(f"O resto é {resto}")
"""

""" ----
dividendo  = int(input("Digite o numero que quer saber de é divisivel: "))
divisor = int(input("Digite o numero pelo qual quer dividir: "))

if dividendo%divisor==0:
    print(f"O numero {dividendo} é divisivel por {divisor}")
else:
    print(
        f"O numero {dividendo}, não é divisivel por {divisor}, pois sobra {dividendo%divisor}")
-----
"""

"""
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"O numero {num1} é maoir que: {num2} e {num3}")
elif num2 > num1 and num2 > num3:
    print(f"O numero {num2} é maoir que: {num1} e {num3}")
elif num3 > num2 and num3 > num1:
    print(f"O numero {num3} é maoir que: {num2} e {num1}")
"""
""" num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

resposta = int(input("Saber maior numero digite 1 ou 2 para menor: "))

if resposta==1:
    if num1 > num2 and num1 > num3:
        print(f"O numero {num1} é maoir que: {num2} e {num3}")

    elif num2 > num1 and num2 > num3:
        print(f"O numero {num2} é maoir que: {num1} e {num3}")

    elif num1==num2 or num2==num3 or num3==num1:
        print(f"Os numeros são iguais")

    else:
         print(f"O numero {num3} é maoir que: {num2} e {num1}")

elif resposta==2:
    if num1 < num2 and num1 < num3:
        print(f"O numero {num1} é menor que: {num2} e {num3}")

    elif num2 < num1 and num2 < num3:
        print(f"O numero {num2} é menor que: {num1} e {num3}")

    elif num1==num2 or num2==num3 or num3==num1:
        print(f"Os numeros são iguais")

    else:
         print(f"O numero {num3} é menor que: {num2} e {num1}")

else:
    print(f"Resposta invalida!") """

#receba dois numeros do usuario
#pergunte se ele quer saber a soma, a subtração, a divisao ou a multiplicação entre esses numeros
# #de a resposta correta

""" 
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("Qual operação você quer fazer?")
print("Soma (+), Subtração(-), Multiplicação (*) ou Divisão (/)")
operador = input("digite o operador: ")

if operador == "+":
    print(f"Soma:{num1+num2}")

elif operador == "-":
    print(f"Subtração:{num1-num2}")

elif operador == "*":
    print(f"Multiplicação:{num1*num2}")

elif operador == "/":
    print(f"Divisão:{num1/num2}")

else:
    print(f"Operador invalido, tente novamente!") """

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

""" sub = num2-num1
if sub<=0:
    sub*=-1

print(sub)
 """
if num1<num2:

    aux=num1
    num1=num2
    num2=aux
print(num1-num2)