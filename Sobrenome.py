def sobrenome():
    nomes = []
    for i in range(0, 5):
        num = input("Digite um nome: ")
        print(num)
        if num == "andre":
            sobre = input("Ola andre, digite seu sobrenome: ")
            nomes.insert(i, sobre)
        else:
            nomes.append(num)
    print(nomes)


sobrenome()
