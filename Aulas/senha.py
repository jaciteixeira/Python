usuario = "Jaci05"
senha = "Jaci12345"

login = input("Digite o login:")
verificarSenha = input("Digite a senha:")

if usuario == login and verificarSenha == senha:
    print("Você está logado")
elif login == usuario and verificarSenha!= senha:
    print("senha invalida")
    trocar = input("Você deseja redefinir a senha?: s ou n: \n")
    if trocar == "s":
        senha = input("Digite a nova senha:")

        ver = input("\n Deseja ver a nova senha?: s ou n:")
        if ver == "s":
            print(f"Senha: {senha}")
        else: print("Senha alterada!")
    else:
        print("Tente novamente!")

else:
    print("Usuario não encontrado!")
