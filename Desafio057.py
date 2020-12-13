n = input('Digite seu nome: ')
s = input('Digite seu sexo [M/f]: ').upper().strip()
while s not in 'MF': #por que nao entra com while s != 'M' or 'F'
    print('Referência incorreta digite M para masculino e F para feminino')
    s = input('Digite seu sexo [M/f]: ').upper().strip()
print(f'Seu nome e {n} e seu sexo e {s}')

