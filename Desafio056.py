somai = 0
maioridade = 0
menoridade = 0
nomevelho = 0
menormulher = 0
for d in range(1, 5):
    print(f'=-=-=-=-=-=- dados do {d} ususario =-=-=-=-=-=-')
    nome = str(input('Digite seu nome: ')).upper()
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    idade = int(input('digite sua idade: '))
    print('===----===----===----===----===---===--===-===')
    somai += idade
    if d == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Fm':
        menormulher += 1
mediaidade = somai / 4
print('=-=-=-=-=-=-=-=-=-DADOS=-=-=-=-=-=-=-=-=-=-=-=')
print(f'A media das idades e {mediaidade} anos')
print(f'O homem mais velho e {nomevelho} e tem {maioridade}')
print(f'Existem {menormulher} mulheres com menos de 20 anos')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
