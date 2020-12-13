from datetime import date
print('=-=-=-' * 20)
print('                                                RECRUTA')
ano = int(input('Informe seu ano de nascimento soldado: '))
atual = date.today( ).year
idade = atual - ano
if idade == 18:
    print('Voce esta apto a se alistar para o serviço mititar \033[4;31mOBRIGATORIO')
elif idade < 18:
    print(f' Aguarde mais {18 - idade} soldado sua vez vai chegar')
else:
    print(f'seu prazo ja passou voce deveria ter se alistado a {idade - 18} anos atras')