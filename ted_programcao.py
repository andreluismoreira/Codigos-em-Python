par = 0
impar = 0
contpar = 0
contimpar = 0
for c in range(1,11):
   v = int(input(f'Digite o seu {c}° valor: '))
   if v % 2 == 0:
       par += 1
       contpar += v
   if v % 2 == 1:
       impar += 1
       contimpar += v
print(f'voce digitou {par} numeros pares e {impar} numeros impares')
print(f'A soma dos numeros pares e {contpar}')
print('A media dos valores impares e {}'.format(contimpar/impar))

