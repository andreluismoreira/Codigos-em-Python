cont = soma = i =maior = menor = 0
q = 'S'
while q in 'S':
    i = int(input('Digite um numero: '))
    q = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += i
    if cont == 1:
        maior = menor = i
    else:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
print(f'Voce digitou {cont} numeros e sua soma e {soma} sua media e {soma/cont}')
print('O maior valor digitado foi {} e o menor valor e {}'.format(maior, menor))

