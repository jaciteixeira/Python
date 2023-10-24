#num = input("diga um numero: ")
# print(num.isnumeric())
# if num.isnumeric():
#     num = int(num)
#     print("parabens")
# else: print("você deveria ter digitado um numero")

'''
num = input("diga um numero: ")

while not num.isnumeric():
   num = input("você deve digitar um numero: ")
print("certinho!")
num = float(num)
print(type(num))
'''

conhecer = input("Quer conhecer a calculadora? S ou N: ")
while conhecer!="s" and conhecer!="n":
    conhecer = input("cara, S ou N?: ")
if conhecer=="s":
    num1 = input("digite o primeiro numero: ")
    num2 = input("digite o segundo numero: ")
    while not num1.isnumeric() or not num2.isnumeric():
        print("eu preciso de numeros!")
        num1 = input("digite o primeiro numero: ")
        num2 = input("digite o segundo numero: ")
    num1 = int(num1)
    num2 = int(num2)
    operador = input("1-Somar \n2-Subtrair \n3-Multi \n4-Div \n5-Sair \nvocê quer: ")
    while operador !=('1'and'2'and'3'):
        operador = input("a opção é 1 , 2 ou 3: ")
    if operador == "1":
        print(f"Soma:{num1 + num2}")
    elif operador == "2":
        print(f"Subtração:{num1 - num2}")
    elif operador == "3":
        print(f"Multiplicação:{num1 * num2}")
    elif operador == "4":
        print(f"Divisão:{num1 / num2}")
    elif operador == "5":
        print(f"Tchauzinho")
else:
    print("você é bobo!")
