cont = soma = 0
while True:
    v = int(input('Digite um valor [digite 990 p/parar]: '))
    if v == 999:
        break
    soma += v
    cont += 1
print(f'Foram digitados {cont} valores e a soma e {soma}')
