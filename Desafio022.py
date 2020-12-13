nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...  ')
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
separa = (nome.split())
print('Seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))




