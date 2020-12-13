import random
import time
print('\033[35m-=-'*20)# a entrada \033[0;34;45m referencia stilo, cor e cor de fundo de um codigo para utilizar olhar tabela
print('\033[30mPensei em um numero, de 0 a 5, tente adivinhar qual numero foi')
print('\033[35m-=-'*20)
numero = int(input('\033[36mQual o seu palpite, vamos ver se voce tem sorte ?? '))
n = random.randint(0, 5)
print('\033[34mProcessando...')
time.sleep(2)
#if numero < 0 and numero > 5:
#   print('Numero invalido digite um numero entre 0 e 5')
if numero == n:
    print('\033[1;32mNão acredito você me venceu, Parabens você acertou !!!')
else:
    print(f'\033[4;31mNao foi dessa vez hahahaha, o numero era {n}, tente novamente !!!')
