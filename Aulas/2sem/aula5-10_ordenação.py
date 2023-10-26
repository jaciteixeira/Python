#SELECTION SORT
def menor_valor(array):
    indice_menor = 0
    menor = array[indice_menor]
    for i in range(len(array)):
        candidato = array[i]
        if candidato< menor:
            menor = candidato
            indice_menor = i
    return indice_menor
#precisa do indice para remoção da lista original
#precisa do indice para colocar o valor certo na nova lista
def seletion_sort_pior(lista):
    lista_ordenada = []
    for i in range(len(lista)):
        local_menor = menor_valor(lista)
        menor_elemento = lista.pop(local_menor)
        lista_ordenada.append(menor_elemento)
        print(f"menor = {menor_elemento}")
        print(f"lista = {lista}")
        print(f"lista ordenada = {lista_ordenada}")
    return lista_ordenada


lista = [2, 1, 7, 3, 5, 6, 4, 8, 9, 0]
lista = [0, 1, 7, 3, 5, 6, 4, 8, 9, 2]
# lista = seletion_sort_pior(lista)
# lista.sort()
# print(lista)

def conta_palavras(texto):
    texto = texto.lower()
    for char in ',.;:/?°"!@#$%¨&*()_-+=§{}[]ªº<>':
        texto = texto.replace(char,'')
    texto = texto.split(" ")
    palavras = {}
    for palavra in texto:
        if palavra not in palavras.keys():
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return palavras

travalinguas= "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
print(conta_palavras(travalinguas))

'''# travalinguas = travalinguas.lower()
# print(travalinguas)
# travalinguas = travalinguas.replace(".",'')
# print(travalinguas)
# travalinguas = travalinguas.split(" ")
# print(travalinguas)'''

letras_zuadas = {
    "áâãàä":"a",
    "ëéèê":"e",
    "íìïî":"i",
    "óòôôö":"o",
    "úùûü":"u"
}

frase = "caminhão e caminhões íntegros no último dia é legal"
for key in letras_zuadas.keys():
    for char in key:
        frase = frase.raplace(char,letras_zuadas[key])
print(frase)

'''
#FORMA INGENUA
for palavra in travalinguas:
    palavras[palavra] = 0
for palavra in travalinguas:
    palavras[palavra] +=1
    print(palavras)'''

'''#NLTK = natural language toolkit
frase = 'danilo está doente'
frase = frase.capitalize()
print(frase)'''
