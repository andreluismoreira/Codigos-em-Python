print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=CALCULADORA DE IMC-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura '))
imc = p / (h * h)
if imc <= 18.5:
    print('Voce esta abaixo do peso, seu imc e {:.2f}'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Voce esta no peso ideal, seu imc e {:.2f}'.format(imc))
elif 25 < imc and imc <= 30:
    print('Voce esta com sobrepeso, seu imc e {:.2f}'.format(imc))
elif 30 < imc and imc <= 40:
    print('Voce esta obeso, seu imc e {:.2f} '.format(imc))
else:
    print('Voce esta com obesidade morbida, seu imc e {:.2f}'.format(imc))
