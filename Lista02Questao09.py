n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 > n2 > n3:
    print(n3, n2, n1)
if n1 > n3 > n2:
    print(n2, n3, n1)
if n2 > n3 > n1:
    print(n1, n3, n2)
if n2 > n1 > n3:
    print(n3, n1, n1)
if n3 > n2 > n1:
    print(n1, n2, n3)
if n3 > n1 > n2:
    print(n2, n1, n1)
else:
    print('Numeros iguais codigo invalido')




