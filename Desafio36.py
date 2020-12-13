print('=-=-'*30)
print('                                            Emprestimo bancario')
print('-=-='*30)
casa = float(input('Qual o valor da casa qe você deseja comprar ? '))
salario = float(input('Quanto você recebe atualmente ? '))
tempofin = int(input('Em quantas vezes voce deseja dividir a casa ? '))
parcelas = casa / tempofin
custo = (salario * 0.3)
if parcelas <= custo:
    print(f'Seu financiamento foi aprovado e suas parcelas serão de {parcelas}')
else:
    print('Infelizmente não foi possivel aprovar seu emprestimo')
