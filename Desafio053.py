frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for frase in range(len(junto) -1, -1, -1):
    inverso += junto[frase]
print(junto, inverso)
if junto == inverso:
    print('Esta frase e um PALINDROMO')
else:
    print('Essa frase nao e um palindromo')

