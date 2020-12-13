clientes = ["Marcelo", "Joana D'arc", "Maria de Fatima"]
produtos = [{"nome": "computador", "preço": 1000.50}, {"nome": "mouse", "preço": 120.10},
            {"nome": "Monitor Ldc", "preço": 999.99}]

listacliente = False
while not listacliente:
    cliente = input("Digite o nome do cliente cadastrado: ")

    if cliente == clientes[0] or cliente == clientes[1] or cliente == clientes[2]:
        listacliente = True
    else:
        print("Cliente nao cadastrado por favor tente novamente")


print("Ola, {} digite abaixo quais os itens e qual a quantidade desejada".format(cliente))
quantComputador = int(input("Digite quantos computadores deseja (preço = 1000.50): "))
quantMouse = int(input("Digite quantos Mouses deseja(preço = 120.10): "))
quantMonitor = int(input("Digite quantos Monitores deseja (preço = 999.99): "))


impComputador = (1000.50 * 0.10) * quantComputador
impMouse = (120.10 * 0.10) * quantMouse
impMonitor = (999.99 * 0.10) * quantMonitor

totalComputador = (quantComputador * 1000.50) + impComputador
totalMouse = (quantMouse * 120.10) + impMouse
totalMonitor = (quantMonitor * 999.99) + impMonitor
total = totalMonitor + totalMouse + totalComputador

print('=' * 30)
print("          NOTA FISCAL")
print("Cliente: " + cliente)
print("Itens Comprados: ")
print("Computador: quantidade {}, valor do imposto {:.2f}, total da compra {:.2f}".format(quantComputador, impComputador, totalComputador))
print("Mouse: quantidade {}, valor do imposto {:.2f}, total da compra {:.2f}".format(quantMouse, impMouse, totalMouse))
print("Monitor: quantidade {}, valor do imposto {:.2f}, total da compra {:.2f}".format(quantMonitor, impMonitor, totalMonitor))
print(f"Total da nota: {total:.2f}")
print("Volte Sempre !!!, {}".format(cliente))