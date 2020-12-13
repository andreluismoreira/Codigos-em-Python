from datetime import date
anoatual = date.today().year
contmaiordeidade = 0
contmenordeidade = 0
for pessoas in range(1, 8):
    i = int(input(f'Qual o ano de nascimento da {pessoas} pessoa: '))
    idade = (anoatual - i)
    if idade >= 21:
        contmaiordeidade += 1
    else:
        contmenordeidade += 1
print(f'Foram listados {pessoas} pessoas e tendo {contmaiordeidade} maior de idade e {contmenordeidade} menor de idade ')
