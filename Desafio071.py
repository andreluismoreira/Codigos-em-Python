print('='*40)
print('{:^40}'.format('BANCO DO ANDRÉ'))
print('='*40)
v = int(input('Qual o valor vc deseja sacar ?: '))
total = v
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$:{ced} ')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre !!!')
