print('=-'*30)
print('                  SEQUENCIA DE FIBONACCI')
print('=-'*30)
x = int(input('Digite quantos numeros voce quer ver: '))
print('-='*30)
t1 = 0
t2 = 1
print('\033[30m{} -> {} '.format(t1, t2), end='')
cont = 2
while cont != x:
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' \033[31mFIM')
