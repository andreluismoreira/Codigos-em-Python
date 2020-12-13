n = int(input(' Digite um numero para saber sua Tabuada: '))
multiplicador = 0
while multiplicador <= 9:
    multiplicador += 1
    tabuada = n * multiplicador
    print('Você digitou {} seus multiplos são, {} X {} = {}' .format(n, n, multiplicador, tabuada))
