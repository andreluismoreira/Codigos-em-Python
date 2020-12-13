n1 = float(input("Digite um numero: "))
n2 = float(input("digite um numero: "))
n3 = float(input("digite um numero: "))
soma = (n2+n3)
if n1 > soma:
    print('O numero digitado {} e maior que a soma de {} e {} que e {}'.format(n1, n2, n3, soma))
else:
    print('O numero {} não e maior que a soma de {} e {} que e {}'.format(n1, n2, n3, soma))
