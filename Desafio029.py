vel = float(input('qual a velocidade do veiculo ? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'\033[1;31mVocê esta acima da velocidade permitida de \033[4:31m80KM/H\033[m e foi \033[4;31mMULTADO\033[m, sua multa sera de {multa}')
print('\033[4;33mDigija com segurança, tenha um Bom Dia')