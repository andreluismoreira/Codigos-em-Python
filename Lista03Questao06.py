n = 0
par = impar = 0
while n < 40:
    n += 1
    if n % 2 == 0:
        par += 1
        print(f'O numero {n} e par ')
    else:
        impar += 1
        print(f'O numero {n} e impar ')


