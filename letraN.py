def main01():
    posicao = int(input("digite sua posicao: "))
    tempoAtendimento = 0
    for i in range(0, posicao - 1):
        tempoEspera = float(input("Digite o tempo medio de espera do cliente {}: ".format(i + 1)))
        tempoAtendimento += tempoEspera
    tempoMedio = tempoAtendimento / posicao
    print("O tempo médio de espera na fila é de: {:.2f} minutos".format(tempoMedio))


def main02():
    posicao = int(input("digite sua posicao: "))
    cont = 0
    tempoAtendimento = 0
    while cont < posicao - 1:
        cont += 1
        tempoEspera = float(input("Digite o tempo medio de espera do cliente {}: ".format(cont)))
        tempoAtendimento += tempoEspera
    tempoTotal = tempoAtendimento / posicao
    print("O tempo médio de espera na fila é de: {:.2f} minutos".format(tempoTotal))


main01()
main02()
