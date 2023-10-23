def conta_palavras(frase):
    for char in ',.!?:;':
        frase = frase.replace(char,'')
    frase = frase.lower()
    dic = {"áàãâ" : 'a','éê' : 'e','í':'i','óôõ':'o','úü':'u'}
    for key in dic.keys():
        for char in key:
            frase = frase.replace(char,dic[key])
    frase = frase.split(" ")
    palavras = {}
    for palavra in frase:
        if palavra not in palavras.keys():
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return palavras

def acha_maior(lista):
    try:
        if type(lista) is not list:
            msg = f"{lista} deveria ser uma lista"
            raise TypeError
        for i in lista:
            msg = f"o valor {i} dentro da lista não é um numero"
            if type(i) not in [int,float]:
                raise TypeError
        indice_maior = 0
        maior = lista[indice_maior]
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                indice_maior = i
        return indice_maior
    except TypeError:
        raise TypeError(msg)

def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

def cadastro():
    for key in dic.keys():
        info = input(f"Diga o novo {key} : ")
        dic[key].append(info)
    return

def obriga_opcao(lista_opcoes,msg,dicionario = None):
    for valor in lista_opcoes:
        print(valor)
    resposta = input(msg)
    while not resposta in lista_opcoes:
        if dicionario:
            for indice,carro in enumerate(dicionario['model']) :
                print(f"{indice} : {carro}")
            resposta = input(msg)
            continue
        for valor in lista_opcoes:
            print(valor)
        resposta = input(msg)
    return resposta
def remocao(dic):
    opcoes = [str(i) for i in range(len(dic['model']))]
    opcao = int(obriga_opcao(opcoes,'Qual carro vc deseja remover ? '))
    for key in dic.keys():
        dic[key].pop(opcao)
    return


frase = "Concluímos que chegamos à conclusão que não concluímos nada. Por isso, conclui-se que a conclusão será concluída quando todas tiverem concluído que já é tempo de concluir uma conclusão."
#print(conta_palavras(frase))

dic = {"model": ["Mazda RX4", "Mazda RX4 Wag", "Datsun 710", "Hornet 4 Drive", "Hornet Sportabout", "Valiant", "Duster 360", "Merc 240D", "Merc 230", "Merc 280", "Merc 280C", "Merc 450SE", "Merc 450SL", "Merc 450SLC", "Cadillac Fleetwood", "Lincoln Continental", "Chrysler Imperial", "Fiat 128", "Honda Civic", "Toyota Corolla", "Toyota Corona", "Dodge Challenger", "AMC Javelin", "Camaro Z28", "Pontiac Firebird", "Fiat X1-9", "Porsche 914-2", "Lotus Europa", "Ford Pantera L", "Ferrari Dino", "Maserati Bora", "Volvo 142E"],"mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4, 33.9, 21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8, 19.7, 15.0, 21.4], "cyl": [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4], "disp": [160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6, 167.6, 275.8, 275.8, 275.8, 472.0, 460.0, 440.0, 78.7, 75.7, 71.1, 120.1, 318.0, 304.0, 350.0, 400.0, 79.0, 120.3, 95.1, 351.0, 145.0, 301.0, 121.0], "hp": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180, 180, 180, 205, 215, 230, 66, 52, 65, 97, 150, 150, 245, 175, 66, 91, 113, 264, 175, 335, 109], "drat": [3.9, 3.9, 3.85, 3.08, 3.15, 2.76, 3.21, 3.69, 3.92, 3.92, 3.92, 3.07, 3.07, 3.07, 2.93, 3.0, 3.23, 4.08, 4.93, 4.22, 3.7, 2.76, 3.15, 3.73, 3.08, 4.08, 4.43, 3.77, 4.22, 3.62, 3.54, 4.11], "wt": [2.62, 2.875, 2.32, 3.215, 3.44, 3.46, 3.57, 3.19, 3.15, 3.44, 3.44, 4.07, 3.73, 3.78, 5.25, 5.424, 5.345, 2.2, 1.615, 1.835, 2.465, 3.52, 3.435, 3.84, 3.845, 1.935, 2.14, 1.513, 3.17, 2.77, 3.57, 2.78], "qsec": [16.46, 17.02, 18.61, 19.44, 17.02, 20.22, 15.84, 20.0, 22.9, 18.3, 18.9, 17.4, 17.6, 18.0, 17.98, 17.82, 17.42, 19.47, 18.52, 19.9, 20.01, 16.87, 17.3, 15.41, 17.05, 18.9, 16.7, 16.9, 14.5, 15.5, 14.6, 18.6], "vs": [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], "am": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], "gear": [4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 4], "carb": [4, 4, 1, 1, 2, 1, 4, 2, 2, 4, 4, 3, 3, 3, 4, 4, 4, 1, 2, 1, 1, 2, 2, 4, 2, 1, 2, 2, 4, 6, 8, 2]}
'''
for key in dic.keys():
    print(key)

for value in dic['hp']:
    print(value)

'''
'''while True:
    msg = 'O que voce gostaria de fazer ? '
    opcao = obriga_opcao(['cadastrar','remover','info mais potente','info menos potente','sair'],msg)
    if opcao == 'cadastrar':
        cadastro()
    elif opcao == 'remover':
        remocao(dic)
    elif opcao == 'info mais potente':
        local_mais_potente = acha_maior(dic['hp'])
        for key in dic:
            print(f"{key} : {dic[key][local_mais_potente]}")
    elif opcao == 'info menos potente':
        local_menos_potente = acha_menor(dic['hp'])
        for key in dic:
            print(f"{key} : {dic[key][local_menos_potente]}")
    else:
        break'''

lista=[1,3,5,6,4,9,7]
print(acha_maior(lista))
