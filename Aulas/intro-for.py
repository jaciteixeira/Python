#EXPLICANDO OS NUMEROS PRIMOS
# num = 83
# i=2
# while i<num:
#     print(f"a divisão de {num} por {i} da resto {num%i}")
#     if num%i==0:
#         print(f"{num} não é primo")
#         break;
#     elif i==num-1:
#         print(f"{num} é primo")
#     i+=1



'''
#ACHANDO OS NUMEROS PRIMOS
num=3
cont_primos=1
while True:
    i=2
    while i<num:
        # print(f"a divisão de {num} por {i} da resto {num%i}")
        if num%i==0:
            # print(f"{num} não é primo")
            break
        elif i>num/2:
            print(f"{num} é primo")
            cont_primos+=1
            break
        i+=1
    num+=1
    if cont_primos==100:
        break
'''


#FORMULA DE FIBONATI
# a=1
# b=1
# cont=0
# while True:
#     while cont<100:
#         c=a+b
#         a=b
#         b=c
#         print(c)
#         cont+=1
#     if cont==100:
#         break

'''
a=1
b=1
cont=0
while True:
    num = a + b
    a = b
    b = num
    i=2
    while i<num:
        # print(f"a divisão de {num} por {i} da resto {num%i}")
        if num%i==0:
            print(f"{num} não é primo")
            break
        elif i>=num**(1/2):
            print(f"{num} é primo")
            cont+=1
            break
        i+=1
    num+=1
    if cont==100:
        break
'''

# senha = input("diga a senha: ")
# i=0
# while senha != password and i<4:
#     password = input("digite a senha: ")
#
#
# for i in range(10):
#     print(i)
#
# frase = "teste"
# for i in range(1, len(frase)):
#     print(frase[i])

for i in range(1,25):
    print(f"5x{i} = {5*i}")