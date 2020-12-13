while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    print('=-=' * 5)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} X {cont} = {n* cont}')
    print('=-='*5)
print('O programa foi encerrado')
