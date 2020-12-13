print('------Maior e Menor valor ------')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
lista = [n1, n2, n3]
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'Entre os valores digitados {lista} o maior e {maior} e o menor e {menor}')
