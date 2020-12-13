def vetor(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma


print(vetor([10, 4, 6, 10, 5, 7, 8, 9, 0, 1]))


