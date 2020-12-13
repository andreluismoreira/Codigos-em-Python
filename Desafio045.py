from random import randint
import time
itens = ('pedra', 'papel', 'tesoura')
print('\033[1;35m<<<<<<<<<<<<<< JO KEM PÔ >>>>>>>>>>>>>>>')
print('\033[1;30m  Vamos jogar pedra papel e tesoura ?  ')
print('\033[1;36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
computador = randint(0, 2)
print("""Suas opções:
[0] pedra
[1] papel
[2] tesoura""")
jogador = int(input('Faça a sua jogada ? '))
print('\033[1;30mJO. ')
time.sleep(1)
print('\033[1;30mKEM.. ')
time.sleep(1)
print('\033[1;30mPOO... ')
time.sleep(1)
print('\033[1;34m=========================================')
print('\033[1;30m        Voce jogou {}'.format(itens[jogador]))
print('\033[1;30m        Computador jogou {}'.format(itens[computador]))
print('\033[1;34m=========================================')
if computador == 0 and jogador == 1:
        print('\033[1;32mVOCÊ GANHOU !!! {} cobre a {}'.format((itens[jogador]), itens[computador]))
elif computador == 0 and jogador == 2:
        print('\033[1;31mVOCÊ PERDEU !!! a {} quebra a {}'.format((itens[computador]), itens[jogador]))
elif computador == 1 and jogador == 0:
        print('\033[1;31mVOCÊ PERDEU !!! o {} embrulha a {} '.format((itens[computador]), itens[jogador]))
elif computador == 1 and jogador == 2:
        print('\033[1;32mVOCÊ GANHOU !!! a {} corta o {}'.format((itens[jogador]), itens[computador]))
elif computador == 2 and jogador == 0:
     print('\033[1;32mVOCÊ GANHOU !!! a {} quebra a {}'.format((itens[jogador]), itens[computador]))
elif computador == 2 and jogador == 1:
        print('\033[1;31mVOCÊ PERDEU !!! a {} corta o {}'.format((itens[computador]), itens[jogador]))
elif jogador > 2 or computador > 2:
    print('0\33[3;31mOPÇÃO INVALIDA REINICIE O JOGO E ESCOLHA UM NUMERO DE 0 A 2', end=(' '))
else:
    print('\033[1;35mEMPATE voce jogou {} e o computador {}'.format((itens[jogador]), itens[computador]))
print('        \033[7;30m >>>>> GaMe OvEr <<<<<\033[m')

