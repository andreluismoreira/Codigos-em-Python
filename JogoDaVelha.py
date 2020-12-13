def mostrarmatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def verificaganhador(matriz, a):
    for i in range(len(matriz)):
        linha = matriz[i][0] + matriz[i][1] + matriz[i][2]
        if linha == "XXX" or linha == "000":
            return a == 1

    for i in range(len(matriz)):
        coluna = matriz[0][i] + matriz[1][i] + matriz[2][i]
        if coluna == "XXX" or coluna == "000":
            return a == 2

    diag01 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diag02 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    if diag01 == "XXX" or diag02 == "XXX" or diag01 == "000" or diag02 == "000":
        return a == 3

    if a == 1:
        print("=-=-=- VOCE VENCEU NA LINHA =-=-=-")
    elif a == 2:
        print("=-=-=- VOCE VENCEU NA COLUNA =-=-=-")
    elif a == 3:
        print("=-=-=- VOCE VENCEU NA DIAGONAL =-=-=-")


def main():
    a = 0
    matriz = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

    while a == 0:

        mostrarmatriz(matriz)

        linha = int(input(" Jogador 01, Digite a linha que deseja jogar dentro do intervalo[0,2]: "))
        coluna = int(input("Digite a coluna que deseja jogar dentro do intervalo[0,2]: "))

        if matriz[linha][coluna] == "-":
            matriz[linha][coluna] = "X"
            verificaganhador(matriz, a)
        elif matriz[linha][coluna] == "0":
            print("o outro jogador ja fez esse movimento")
        else:
            print("voce ja fez essa jogada")

        mostrarmatriz(matriz)

        linha = int(input("Jogador 02, Digite a linha que deseja jogar dentro do intervalo[0,2]: "))
        coluna = int(input("Digite a coluna que deseja jogar dentro do intervalo[0,2]: "))

        if matriz[linha][coluna] == "-":
            matriz[linha][coluna] = "0"
            verificaganhador(matriz, a)
        elif matriz[linha][coluna] == "X":
            print("o outro jogador ja fez esse movimento")
        else:
            print("voce ja fez essa jogada")

    verificaganhador()


main()
