from time import sleep
primeiro = int(input('Digite seu 1° numero: '))
segundo = int(input('Digite seu 2° numero: '))
opcao = 0
while opcao != 5:
    print('''O que voc deseja realizar:
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos numeros
            [5] Finalizar''')
    opcao = int(input('Escolha entre as opções acima: '))
    if opcao == 1:
        print(primeiro + segundo)
    elif opcao == 2:
        print(primeiro * segundo)
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O numero {primeiro} e maior que {segundo}')
        elif segundo > primeiro:
            print(f' o {segundo} e maior que {primeiro}')
        else:
            print('os numeros digitados sao iguais')
    elif opcao == 4:
        primeiro = int(input('Digite seu novo 1° numero: '))
        segundo = int(input('Digite seu novo 2° numero: '))
    elif opcao == 5:
        print('\033[30mfinalizando...\033[m')
    else:
        print('Voce digitou uma opção invalida por favor digite novamente')
sleep(2)
print('\033[31moperação finalizada\033[m')
