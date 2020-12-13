
def main ():
    matriz = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]
    matrizsete = []
    for i in range(len(matriz)):
        matriz = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]
        for j in range(0,3):
           sete = matriz[i][j] * 7
           matrizsete.append(sete)


    return print(matrizsete)


main()