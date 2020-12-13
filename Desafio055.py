menor = 0
maior = 0
for peso in range(1, 6):
    p = float(input(f'Digite o peso do {peso}° usuario: '))
    if peso == 1:
        menor = p
        maior = p
    else:
        if p > maior:
          maior = p
        if p < menor:
          menor = p
print(f'O menor peso e {menor} Kg e o maior e {maior} Kg')
