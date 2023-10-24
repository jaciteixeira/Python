# indice = 0
# lista = [1,625,65,2541,15,565,515,15,36,54,100,326]
# for num in lista:
#     if num==100:
#         indicedo100=indice
#     indice+=1
#     print(f"O numero 100 está na posição{indicedo100+1}°")

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