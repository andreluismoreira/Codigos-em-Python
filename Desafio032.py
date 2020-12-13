ano = int(input('digite um ano para saber se eLe e BISSEXTO: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO ')
else:
    print(f' O ano {ano} nao e bissexto')
