preco = float(input('Digite o valor do Produto em reais, R$:'))
descontaco = (preco * 5 / 100)
desconto = preco - descontaco
print(' O preço do produto foi {} com o desconto de 5% fica por {} desconto de {} R$'.format(preco, desconto, descontaco))
