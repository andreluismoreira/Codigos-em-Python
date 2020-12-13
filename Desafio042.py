oposto = int(input('Digite um numero: '))
adjacente = int(input('Digite um numero: '))
hip = int(input('Digite um numero: '))
if ((oposto + adjacente) > hip) and ((hip + oposto) > adjacente) and ((hip + adjacente) > oposto):
    print('As medidas dadas podem formar um triagulo ', end='')
    if oposto == adjacente == hip:
        print('Equilatero')
    elif oposto != adjacente != hip != oposto:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Essas medidas nao formam um triagulo')
