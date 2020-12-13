print('---===---===CALCULADORA DE FATORIAL!---===---===')
num = int(input('Digite um numero para saber seu fatorial: '))
cont = num
fatorial = 1
while cont != 0:
    print(cont, end=" ")
    print('x' if cont > 1 else '=', end=" ")
    fatorial *= cont
    cont += -1
print(fatorial)
