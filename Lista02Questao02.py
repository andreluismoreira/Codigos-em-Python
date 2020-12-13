nota1 = float(input('digite sua 1° nota: '))
nota2 = float(input('digite sua 2° nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('Sua media e {} e você esta APROVADO'.format(media))
elif media <= 4:
    print('Sua media foi {} você esta REPROVADO'.format(media))
else:
    print('Sua media foi {} você esta na PROVA FINAL'.format(media))
