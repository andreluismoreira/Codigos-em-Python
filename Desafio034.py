salario = float(input('Digite seu salario: '))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print(f'Seu salario e de {salario} e você ira receber um aumento de \033[1:31m10%\033[m ficando com {aumento}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Seu salario e de {salario} e voce recebeu um aumento de \033[1:32m15%\033[m ficando com {aumento}')
