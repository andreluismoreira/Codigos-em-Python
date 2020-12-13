print('----Conversor de Moedas----')
valor = float(input('Quanto dinheiro voce tem na carteira ? R$:'))
dolar = 4.65
euro = 5.22
conversao = valor / dolar
conversao2 = valor / euro
print(' Voce tem R${:.2f} que e equivalente a U${:.2f} dolares'. format(valor, conversao))
print(' Voce tem R${:.2f} que e equivalente a U${:.2f} euros'. format(valor, conversao2))
