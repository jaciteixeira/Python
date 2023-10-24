def par_ou_impar(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num%2 ==0:
            pares+=1
        else:
            impares+=1
    return [pares,impares]

#resultado = par_ou_impar([2,5,8,9,12])
#print(resultado)
#qtd_pares = resultado[0]
#qtd_impares = resultado[1]
#print(qtd_pares)
#print(qtd_impares)

#faÃ§a uma funÃ§Ã£o que recebe uma lista de numeros e retorna o indice do maior numero
#faÃ§a uma funÃ§Ã£o que recebe uma lista de numeros e retorna o indice do menor numero

def retorna_indice_maior(lista):
    maior = lista[0]
    indice_maior = 0
    for i in range(len(lista)):
        #print(f"Vou testar se lista[{i}], ou seja {lista[i]} > {maior}")
        if lista[i] > maior:
            #print(f"O maior valia {maior} no indice {indice_maior}")
            maior = lista[i]
            indice_maior = i
            #print(f"O maior passa a valer {maior} no indice {indice_maior}")
    return indice_maior

def retorna_indice_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range(len(lista)):
        #print(f"Vou testar se lista[{i}], ou seja {lista[i]} > {maior}")
        if lista[i] < menor:
            #print(f"O maior valia {maior} no indice {indice_maior}")
            menor = lista[i]
            indice_menor = i
            #print(f"O maior passa a valer {maior} no indice {indice_maior}")
    return indice_menor
#local_maior = retorna_indice_maior(numeros)
#print(numeros[local_maior])
#local_menor = retorna_indice_menor(numeros)
#print(numeros[local_menor])



#local_mais_caro = retorna_indice_maior(precos)
#print(vinhos[local_mais_caro])
#local_mais_barato = retorna_indice_menor(precos)
#print(vinhos[local_mais_barato])

def cadastra_vinho(vinhos,qtd):
    for i in range(qtd):
        nome = input("Diga o nome do vinho : ")
        vinhos.append(nome)
    return vinhos

def cadastra_preco(precos,qtd):
    for i in range(qtd):
        nome = input("Diga o preÃ§o do vinho : ")
        precos.append(nome)
    return precos

def input_numerico(frase):
    num = input(frase)
    while not num.isnumeric():
        print("Voce nao digitou um inteiro!")
        num = input(frase)
    return int(num)

def soma_lista(numeros):
    soma = 0
    print("vim pra funÃ§Ã£o soma")
    for num in numeros:
        soma+=num
    return soma
def valor_total(numeros):
    vt = soma_lista(numeros)
    print(f"Voce gastou R${vt},00 reais")
    return

def media(numeros):
    print("to na funÃ§Ã£o media")
    soma = soma_lista(numeros)
    media = soma/len(numeros)
    return media

def verifica_opcoes(msg,opcoes):
    opcao = input(msg)
    while not opcao in opcoes:
        print("Voce deve digitar uma opcao vÃ¡lida!")
        opcao = input(msg)
    return opcao

valor_precos = [20,40,50,15,25,100,10]


#qtd = input_numerico("Qts vinhos voce quer cadastrar ? ")
#ano_nascimento = input_numerico("Que ano vc nasceu ? ")

#nome_vinhos = cadastra_vinho(nome_vinhos,qtd)
#precos = cadastra_preco(valor_precos,qtd)
#print(nome_vinhos)
#print(valor_precos)

#faÃ§a uma funÃ§Ã£o que pede numeros ao usuario e retorna o numero somente quando for um int
#faÃ§a uma funÃ§Ã£o que acha o preco medio dos vinhos

opcoes = ["sim","nao"]
#resposta = verifica_opcoes("Voce quer conhecer a vinheria (sim/nao)? ",opcoes)
#resposta = input("Voce quer conhecer a vinheria ? ")
#while not resposta in opcoes:
#    resposta = input("Voce quer conhecer a vinheria ? ")

nome_vinhos = ["rose","tinto","branco","seco","suave","suavinho","licoroso"]
#qual_vinho = verifica_opcoes("Diga qual vinho vc quer : ",nome_vinhos)
#qual_vinho = input("Diga qual vinho vc quer : ")
#while qual_vinho not in nome_vinhos:
#    qual_vinho = input("Diga qual vinho vc quer : ")

opcoes = ["continuar","sair"]
#continua_ou_nao = verifica_opcoes("Digite continuar compra ou sair",opcoes)
#continua_ou_nao = input("Digite continuar compra ou sair")
#while not continua_ou_nao in opcoes:
#    continua_ou_nao = input("Digite continuar compra ou sair")
#qtd = input_numerico(f"Qts garrafas de {qual_vinho} vc quer ?")

#carrinho = [30,60,70]
#gasto_total = soma_lista(carrinho)
#print(gasto_total)

nome = "danilo"

match nome:
    case "danilo":
        print("Oi danilo")
    case "gabriel":
        print("oi gabriel")