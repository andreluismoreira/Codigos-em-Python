numero = int(input("digite um numero inteiro para saber seu fatorial: "))

def For ():

    fatorial = numero
    for i in range(1, numero):
        fatorial = fatorial * i
    return print(fatorial)


def While ():

    cont = 1
    fatorial = 1
    while cont <= numero:
        fatorial *= cont
        cont += 1
    return print(fatorial)


For()
While()