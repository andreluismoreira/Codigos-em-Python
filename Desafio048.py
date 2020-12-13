acumulador = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        acumulador += c
        contador += 1
print('foram somados {} numeros e o resultado e {}'.format(contador, acumulador))
