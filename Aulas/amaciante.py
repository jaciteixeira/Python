"""
preco_amaci = 0.5
quant_amaci = int(input("Quantos amaciantes?: "))
cadastro = input("Existe cadastro? S ou N?: ")

while (cadastro!="s" and5 cadastro!="n"):
    print("Escolha Invalida!")
    cadastro = input("Existe cadastro? S ou N?: ")

if cadastro=="s" and quant_amaci>100:
    print("Parabéns! Você teve desconto. ")
    preco_amaci = 0.30
elif cadastro== "s" or quant_amaci>=100:
    print("Parabéns! Você teve desconto. ")
    preco_amaci = 0.35

preco_final = preco_amaci * quant_amaci
print(f"O amaciante custou: R${preco_amaci}")
print(f"Valor da compra: R${preco_final:.2f}")
"""

'''
i=2
while i<=10:
    if i%2==0:
        print(f"{i} é par")
        i+=1
'''

'''
vezes=0
while vezes<3:
    letra = input("digite uma letra: ")
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("Digitou uma vogal!")
    else:
        print("Digitou uma consoante!")
    vezes+=1
    if vezes==3:
        print("\nObrigada, Tchau")
'''

'''
pergunta = input("quer descobrir os pares entre 1 e 20?\ns ou n: ")
while pergunta!="s" and pergunta!="n":
    pergunta = input(f"{pergunta} não é valido, digite novamente: ")

if pergunta=="s":
    i=1
    while i<=20:
        if i%2==0:
            print(f"{i} é par")
        i+=1
elif pergunta=="n":
    print("Você é chato!")
'''

vezes = float(input("quantas palavras?: "))
i=1
nova_frase= input("Digite uma palavra: ")+ " "
while i<vezes:
    frase= input("Digite a outra palavra:")
    nova_frase+=frase + " "
    i+=1
print(nova_frase)
