cont = soma = i = 0
i = int(input('digite um numero [999 para parar]: '))
while i != 999:
    cont += 1
    soma += i
    i = int(input('digite um numero [999 para parar]: '))
print(f'voce digitou {cont} numeros e sua soma e {soma}')

