num = int(input('Digite um numero para analise: '))
print('Analisando...')
if num % 2 == 0:
    print(f'O numero {num} e \033[1;33mPAR')
else:
    print(f'O numero {num} e \033[1;34mIMPAR')
