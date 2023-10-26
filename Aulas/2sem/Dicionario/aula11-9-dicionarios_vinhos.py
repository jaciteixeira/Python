import pandas as pd

def forca_resposta(msg,lista_opcoes):
    resp = input(msg)
    while resp not in lista_opcoes:
        print("Digite uma resposta valida! ")
        resp = input(msg)
    return resp

def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

vinhos = {
    'tipo' : ['tinto', 'rosé', 'seco', 'branco', 'suave'],
    '% alcoólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preco' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','françês','italiano','jundiaiense']
}

lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))] #compreenssão de listas

compra = {
    'endereco': {
            'Rua': '',
            'Nº': '',
            'Cidade': '',
            'Estado': '',
            'complemento': ''},
    'valor total':0,
    'vinhos': {}
}
papel = forca_resposta("Você é cliente ou fincinario? (c/f) :", ['c','f'])

if papel == 'c':
    print('Seja bem vindo!')
    for key in compra['endereco'].keys():
        info = input(f'Diga seu/a {key}: ')
        compra['endereco'][key] = info
    while True:
        print('Essas são as nossas opções de vinhos: ')

        for i in range(len(vinhos['tipo'])):
            print(f'{i} - {vinhos["tipo"][i]}')

        opcao = int(forca_resposta("Qual vinho lhe interessou mais : ", lista_vinhos))

        for key in vinhos.keys():
            print(f"{key}: {vinhos[key][opcao]}")

        comprar = forca_resposta("Vai comprar? (s/n) :", ['s','n'])
        if comprar == 's':
            compra['valor total'] += vinhos['preco'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1

        continuar = forca_resposta("Você gostaria de ver mais vinhos? (s/n) :", ['s','n'])
        if continuar =='s':
            continue

        else:
            print("Obrigado pelo compra!")
            printa_dicionario(compra)
            break


else:
    '''
    opcoes = int(forca_resposta(f"1 - Cadrastrar vinho\n2 - Alterar preço\n3 - Remover vinho\nDigite umas das opções: ",['1','2','3']))
    '''

    opcoes= ['alterar preço', 'cadastrar', 'remover']
    print("Essas são as opções: ")
    for i in range(len(opcoes)):
        print(f'{i} - {opcoes[i]}')

    opcao = forca_resposta("Digite umas das opções: ",['0','1','2'])
    if opcao == '0':
        for i in range(vinhos['tipo']):
            print(f"{i} - {vinhos['tipo'][i]}")
        alterar = forca_resposta("Qual vinho será alterado?", lista_vinhos)
        novo_valor = float(input("Diga o novo valor: "))
        vinhos['preco'][alterar] = novo_valor


    elif opcao == '1':
        for key in vinhos.keys():
            novo_vinho= input(f"Digite o/a {key}:")
            vinhos[key].append(novo_vinho)

    else:
        for i in range(len(vinhos['tipo'])):
            print(f'{i} - {vinhos["tipo"][i]}')
        removido = int(forca_resposta("Qual vinho quer remover : ", lista_vinhos))

        for key in vinhos.keys():
            vinhos[key].pop(removido)

    # printa_dicionario(vinhos)
    impressao_vinhos = pd.DataFrame(vinhos)
    print(impressao_vinhos)


