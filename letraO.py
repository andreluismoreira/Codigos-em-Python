def main01():
    numInicio = int(input("digite um numero inicial: "))
    numSaida = int(input("digite um numero de termino: "))

    for i in range(numInicio, numSaida + 1):
        print(i * i, end=" ")


def main02():
    numInicio = int(input("digite um numero inicial: "))
    numSaida = int(input("digite um numero de termino: "))
    cont = numInicio

    while cont <= numSaida:
        print(cont * cont, end=" ")
        cont += 1


main01()
main02()