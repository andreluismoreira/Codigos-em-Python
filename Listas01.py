continua = 'S'
lista = []
while continua == 'S':
    lista.append(input('Digite um numero: '))
    continua = input('Deseja continuar (s/n) ?: ').upper()
print(lista)
for i in range(len(lista)):
    lista[i] = lista[i] + 1
print(lista)
