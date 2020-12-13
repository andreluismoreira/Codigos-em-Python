acum = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c} numero: '))
    if n % 2 == 0:
        acum += n
        soma += 1
print(f'Você digitou {soma} numeros PARES e a soma e: {acum}')

