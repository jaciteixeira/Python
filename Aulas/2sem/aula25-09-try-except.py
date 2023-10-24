lista = [54,3,56,2,4,7,6,34]
tentativa=0
while tentativa < 3:
    try:
        tentativa+=1
        print(f"Tentativa nº: {tentativa} ")
        indice = int(input("Diga um numero: "))
        print(lista[indice])
        break
    except IndexError as e:
        print(e)
        print(f"Esse indice não existe! valor maximo é: {len(lista)-1}")
    except ValueError as erro:
        print(erro)
        print("Deve ser um numero!")
    # finally:
    #     print(f"Tentativa nº: {tentativa} ")

    except:
        print(f"Alguma coisa aconteceu!")
