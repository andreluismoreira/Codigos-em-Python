dia = int(input('Quantos dias o carro passou em sua posse ? '))
km = float(input('Quantos Km foram rodados ? '))
valor = (dia*60) + (km * 0.15)
print('O carro foi utilizado por {} dias e rodou {:.2f} quilometros, com custo de aluguel de {:.2f}'.format(dia, km, valor))
