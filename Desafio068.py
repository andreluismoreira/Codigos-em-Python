from random import randint
from time import sleep
print('-=-'*15)
print('Vamos jogar par ou impár ?')
print('Digite um numero de 0 a 10')
print('=-='*15)
cont = 0
while True:
    n = int(input('Digite um numero: '))
    c = randint(0, 10)
    total = n + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer Par ou Impar[P/I]: ')).upper().strip()[0]
        sleep(2)
    print(f'Deu Par !!!' if total % 2 == 0 else 'Deu Impar !!!')
    print(f'Voce digitou {n} e o computador {c} total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            cont += 1
        else:
            print('Você Perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!!!')
            cont += 1
        else:
            print('Voce perdeu')
            break
    print("Vamos jogar novamente.....")
print(f'Game Over,seu total de vitórias foi {cont}')
