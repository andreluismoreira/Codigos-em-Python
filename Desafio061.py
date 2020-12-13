num = int(input('Digite seu primeiro terno: '))
r = int(input('Digite a razão: '))
q = int(input('Quantas vezes voce quer ver a progressão: '))
cont = 0
razao = num
while cont != q:
    print('{} -> '.format(razao), end=' ')
    razao += r
    cont += 1
print('FIM')
