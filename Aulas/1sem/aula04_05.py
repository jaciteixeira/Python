lista = [1,2,4567, 4.5, ["aeiou00"],"wasd", True, [i for i in range(10) if i%2==0]]
for elem in lista:
    print(type(elem))
for i in range(len(lista)):
    print(lista[i])
