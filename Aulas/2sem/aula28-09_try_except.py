'''
while True:
    try:
        a = int(input("Diga o primeiro numero : "))
        b = int(input("Diga o segundo numero : "))
        print(b / a)
        break
    except ZeroDivisionError:
        print(f"Primeiro numero não pode ser zero!!!")
    except ValueError:
        print(f"Ambos os numeros devem ser inteiro!!!")
'''

'''dic = {
    'sao paulo':'campeão',
    'palmeiras':'não tem mundial',
    'corinthians':'sem estádio',
    'santos':'idoso'
}
while True:
    time = input("diga o time: ")
    try:

        print(f"Informações do {time}: {dic[time]}")
        break
    except KeyError:
        print(f'Não existe "{time}" no banco de dados!')'''

'''dic = {
    1:'um',
    2:'dois',
    3:'tres',
    17:'dezesete',
    20:'vinte'
}

# while True:
#     num = input("Diga um numero para converter para extenso: ")
#     while not num.isnumeric():
#         print("Numero!!!")
#         num = input("Diga o numero: ")
#     num = int(num)
#     if num in dic.keys():
#         print(dic[num])
#         break

while True:
    print(f"{dic.keys()}")

    num = input("Diga um numero para converter para extenso\n-> ")
    try:
        num = int(num)
        extenso = dic[num]
        # print(dic[num])
        # break
    except ValueError:
        print("Numero!!!")
    except KeyError:
        print("Digite uma das opções!!!")
    else:
        print(f"O {num} por extenso é {extenso}")
        break'''

dic = {
    1:['um','one','uno'],
    2:['dois','two','dos'],
    3:['três','three','tres']
}

# def validar_numero(a,b):

while True:
    try:
        flag = 'O numerodeve ser 1, 2 ou 3'
        opcao = int(input(' diga um numero de 1 a 3 para ser traduzido -->'))
        flag = '\n0- pt-br\n1- inglês\n2-espanhol\n'
        idioma = int(input('0- pt-br\n1- inglês\n2-espanhol\n->'))

        print(f"Tradução: {dic[opcao][idioma]}")
        break

    except KeyError:
        print(f"deve ser um desses {dic.keys()}")
    except ValueError:
        print(f"idiomas disponiveis {flag}")
    except IndexError:
        print(flag)






