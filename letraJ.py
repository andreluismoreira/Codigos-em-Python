def main ():
    nome = input("digite seu nome: ")
    sexo = input("digite o seu sexo: ").upper()

    print("ola,", nome)

    if sexo[0] == "F":
        print("seu Sexo e feminino")
    elif sexo[0] == "M":
        print("Seu sexo e masculino")
    else:
        print("Seu genero e indefinido")


main()