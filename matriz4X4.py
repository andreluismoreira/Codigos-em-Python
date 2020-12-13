
def main():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            num = input("digite um valor para a matriz: ")
            linha.append(num)
        matriz += [linha]

    return print(matriz)


main()