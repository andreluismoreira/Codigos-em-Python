preço = float(input('Qual o preço so produto ? '))
pag = str(input('Qual a condição de pagamento [ dinheiro, debito, credito, parcelado] ? ')).upper()
if pag == 'DINHEIRO':
    print(f' Voce escolheu pagar a vista e tera 10% de desconto pagando {preço - (preço* 0.1)}')
elif pag == 'DEBITO':
    print(f'Voce escolheu pagamento em debito e tera 5% de desconto pagando {preço - (preço * 0.05)}')
elif pag == 'CREDITO':
    print(f'Voce escolheu pagar no credito e pagara {preço}')
else:
    print(f'Voce escolheu pagar parcelado e pagara {preço + (preço * 0.2)}')
