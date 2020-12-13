
def nomes():
    registros = []

    for i in range(0, 5):
        entrada = input("digite um nome: ")
        registros.append(entrada)

    print(registros)

    entrada1 = input("digite um nome para o final da lista: ")
    registros.append(entrada1)

    entrada2 = input("digite um nome para a 2 posição da lista: ")
    registros.insert(1, entrada2)

    print(registros)


nomes()
