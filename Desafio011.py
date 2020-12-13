print('---Pintando uma parede---')
largura = float(input('Digite a largura da sua parede em metros: '))
comprimento = float(input('Digite o comprimento da parede em metros: '))
area = largura*comprimento
tinta = area/2
print('A largura dada foi {} o comprimento dado foi {} com area de {}, precisando de {} litros de tinta'.format(largura, comprimento,area, tinta))
