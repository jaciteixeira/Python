'''

soma=1
i=0
while i<=100:
    soma+=soma
    i+=1
print(f"A soma de todos os numeros de 1 a 100: {soma}")
'''


'''
qtd_palavra = int(input("quantas palavras?: "))
vezes = 0
frase = ""
while vezes<qtd_palavra:
    palavra = input("digite outra palavra: ")
    frase +=palavra + " "
    vezes+=1
print(f"Frase: {frase}")
'''


#MINHA SOLUÇÃO
'''
usuario = "Jaci05"
senha = "1234"
i=0
verificarUsuario = input("Digite o login:")
verificarSenha = input("Digite a senha:")

if verificarSenha==senha and verificarUsuario==usuario:
    print("Logado!")
elif verificarUsuario==usuario and verificarSenha!=senha:
    print(f"Senha Incorreta, tente novamente")
    i=0
    while i<3:
        i+=1
        if verificarSenha!=senha:
            print(f"Tentativas Restante: {3-i}")
            verificarSenha = input(f"digite a senha:")
redefinir = input(f"Tentou muitas vezes, deseja redefinir a senha? S ou N:")

while redefinir!="s" and redefinir!="n":
    redefinir = input("Invalido! digite s ou n:")
if redefinir=="s":
    senha=input("digite a nova senha: ")
    print(f"Senha: {senha}")
elif redefinir=="n":
    print("Ok")
'''



'''SOLUÇÃO PROFESSOR'''
# usuario = "Jaci05"
# senha = "1234"
# i=0
# while True:
#     verificarUsuario = input("Digite o login:")
#     verificarSenha = input("Digite a senha:")
#     if verificarSenha == senha and verificarUsuario == usuario:
#         print("Logado!")
#         break
#     else:
#         i+=1
#         print(f"errou, tentativas: {3-i}")
#     if i==3:
#         print("sai hacker")
#         break


maca=0
tomate=0
banana=0
while True:
    print(f"Maçã \nTomate \nBanana \nMelancia ")
    opcoes = input("oque quer comprar: ")
    match opcoes:
        case "1":
            maca+=5
        case 'fim':
            print(opcoes)










