'''
print("Hello");
primeira_palavra =("Olá")
segunda_palavra = ("Mundo")

sentenca = primeira_palavra + " " + segunda_palavra
print("Primeiro print" , sentenca)
print("\n")
var1 = "Meu"
var2 = "nome"
var3 = "é"
var4 = "Sei lá"

sentenca = var1 + " " + var2 + " " + var3 + " " + var4

print("Segundo print" , sentenca)
'''
#use essa estrutura para escrever "olá, sou tal, tenho tantos anos"

"""sentenca = "Olá, "
print("Primeiro print:" , sentenca)
sentenca+= "meu nome é Jaci,"
print("Segundo print:" , sentenca)
sentenca+= "tenho tal idade"
print("Terceira print" , sentenca)"""

"""trabalho = input("digite a profissão:")
print(f"{sentenca} e sua profissão é{trabalho}")"""

"""num1 = "17"
num2 = "55"
print(type(num1))
print(type(num2))
print(f"o tipo de num1 é {type(num1)}, o tipo de num2 é {type(num2)}")
soma = num1 + num2
print(f"essa é a soma de strings: {soma}")
num1 = int(num1)
num2 = int(num2)
print(f"o tipo de num1 é {type(num1)} e o tipo de num2 é {type(num2)}")
soma = num1 + num2
print(f"e a soma é: {soma}")"""

"""valor=input("digite o valor do produto:")
valor1=input("digite o valor o outro produto:")
print(f"comparação dos produtos: {valor} é maoir que {valor1} ? : {valor>valor1}")
print(f"comparação dos produtos: {valor} é menor que {valor1} ? : {valor<valor1}")"""

a=input("digite um numero:")
b=input("digite mais um numero:")

if b==a:
        print("são iguais")

elif a>b:
    print("a é maior que b")

elif b>a:
    print("b é maior que a")