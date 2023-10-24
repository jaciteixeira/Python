"""
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

escolha = float(input("Digite 1 para saber se é maior e 2 para menor: "))

if escolha == 1:
    if num1 > num2 and num1 > num3:
        print(f"O maior numero é {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"O maior numero é {num2}")
    else:
        print(f"O maior numero é {num3}")

elif escolha==2:
    if num1 < num2 and num1 < num3:
        print(f"O menor numero é {num1}")
    elif num2 < num1 and num2 < num3:
        print(f"O menor numero é {num2}")
    else:
        print(f"O menor numero é {num3}")

else:
    print("Escolha invalida, tente novamente.")


preco_amaci = 0.5
quant_amaci = int(input("Quantos amaciantes?: "))
cadastro = input("Existe cadastro? S ou N?: ")

if cadastro== "s" or quant_amaci>=100:
    print("Parabéns! Você teve desconto. ")
    preco_amaci = 0.35

preco_final = preco_amaci * quant_amaci
print(f"Valor da compra: R${preco_final:.2f}")
"""

usuario = "Jaci05"
senha = "j123"

verificarUsuario = input("Digite o usuario: ")
verificarSenha = input("Digite a senha: ")


if verificarUsuario == usuario and verificarSenha == senha:
    print("Logado!")

elif verificarUsuario==usuario and verificarSenha != senha:
    
    # vezes = 0
    # while vezes<=3 or verificarSenha!=senha :
    #     vezes+=1
    #     print("Senha incorreta!")
    #     verificarSenha = input("Digite a novamente a senha:")

    trocar = input("Você deseja redefinir a senha?: \n s ou n:")

    if trocar == "s":
        senha = input("Digite a nova senha:")
    elif trocar == "n":
        print("Tente novamente")
    ver = input("Deseja ver a nova senha? S ou N: ")
    if ver == "s":
        print(f"Senha: {senha}")
    else :
        print("Senha Alterada!")
elif verificarUsuario!=usuario and verificarSenha!=senha:
    print("SAI HACKER")

