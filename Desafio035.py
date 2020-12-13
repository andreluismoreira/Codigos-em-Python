print('=-=-=-Regra do Triangulo-=-=-=')
n1 = int(input('Digite o primeiro lado do seu triangulo: '))
n2 = int(input('Digite o segundo lado do seu triangulo: '))
n3 = int(input('Digite o terceiro lado do seu triangulo: '))
if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n2 + n1):
    print(' esses lados sao formadores de um triagulo')
else:
    print('essas medidas nao formam um triagulo')
