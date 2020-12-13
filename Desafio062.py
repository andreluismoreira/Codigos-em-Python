num = int(input('Digite seu primeiro terno: '))
r = int(input('Digite a razão: '))
cont = 1
razao = num
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(razao), end=' ')
        razao += r
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos a mais voce quer mostrar: '))
print(f'voce digitou {num} com razão {r} com uma PA de {total} vezes')
print('FIM')
