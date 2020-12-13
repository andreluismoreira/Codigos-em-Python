print('*'*40)
print('{:^40}'.format('Lojão da economia'))
print('*'*40)
soma = mmil = menor = maior = cont = 0
barato = ' '
while True:
    produto = str(input('Produto: '))
    custo = int(input('Preço R$: '))
    soma += custo
    cont += 1
    if custo > 1000:
        mmil += 1
    if cont == 1:
        menor = custo
        maior = custo
        barato = produto
    else:
        if custo > maior:
            maior = custo
        if custo < menor:
            menor = custo
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N] ?: ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {soma}')
print(f'{mmil} produtos custaram mais de 1000 R$')
print(f'O produto mais barato foi {barato} por {menor}')
print(f'O produto mais caro custa {maior}')







