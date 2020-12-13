numero = int(input('Digite um numero inteiro: '))
cont = 1
resultado = 0
while cont <= numero:
    resultado += cont
    cont += 1
    print('Você digitou {} e a soma dos seus antessesores e {}'.format(numero, resultado))
