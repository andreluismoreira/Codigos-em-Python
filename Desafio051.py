print('-=-=-=-=-=Calculadora de PA=-=-=-=-=-')
r = int(input('Digite um valor: '))
p = int(input('Digite sua PA/Razão: '))
for (c) in range(1, 11):
    pa = r + (c - 1) * p
    print(f'{pa}', end= (' -> '))
print('ACABOU')