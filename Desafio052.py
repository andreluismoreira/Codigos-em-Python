print('=-=-=-=-=-> Numeros Primos <=-=-=-=-=-')
num = int(input('Digite um numero: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, div))
if div == 2:
    print(f'O numero {num} so e diviSivel po 1 e ele mesmo portanto ele e um NUMERO PRIMO')
else:
    print(f'O numero {num} tem varios divisiveis e por isso nao e PRIMO')
print('<-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=->')