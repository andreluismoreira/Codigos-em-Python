numalunos = 5
nomes = []
notas = []
media = 0
for i in range(numalunos):
    nomes.append(input('Digite seu nome: '))
    notas.append(float(input('Digite a nota de ' + nomes[i] + ': ')))
    media = media + notas[i]
media = media/numalunos
print('A media dos alunos e: ', media)
for i in range(numalunos):
    if notas[i] >= media:
        print('Parabéns !!!,', nomes[i])





