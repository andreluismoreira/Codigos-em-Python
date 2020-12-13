import random
import time
palpites = 1
print('\033[35m-=-'*20)# a entrada \033[0;34;45m referencia estilo, cor e cor de fundo de um codigo para utilizar olhar tabela
print('\033[30mPensei em um numero, de 0 a 10, tente adivinhar qual numero foi')
print('\033[35m-=-'*20)
numero = int(input('\033[36mQual o seu palpite, vamos ver se voce tem sorte ?? '))
n = random.randint(0, 10)
print('\033[1;30mProcessando...\033[m')
time.sleep(2)
while numero != n:
    palpites += 1
    if numero > n:
        numero = int(input('\033[31mQuase!!!, pensei em um numero um pouco menor, tente novemente: \033[m'))
        print('\033[1;30mProcessando...\033[m')
        time.sleep(2)
    elif numero < n:
        numero = int(input('\033[31mQuase!!!, pensei em um numero um pouco maior, tente novamente: \033[m'))
        print('\033[1;30mProcessando...\033[m')
        time.sleep(2)
print('\033[32mParabéns!!! voce acertou, com {} palpites\033[m'.format(palpites))
