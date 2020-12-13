lista = ('zero', 'um ', 'dois', 'três', 'quatro',' cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze',' doze', 'treze', 'quatorze', 'quinze',' dezesseis', 'dezessete',' dezoito', 'dezenove',' vinte')
while True:
    c = int(input('digite um numero entre 0 e 20: '))
    if 0 <= c <= 20:
        break
    else:
        print('Tente novamente.', end='')
print(f'Voce digitou o numero {lista[c]}')

