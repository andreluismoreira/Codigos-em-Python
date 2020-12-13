def main():
    lista = [['1', '2', '3', '4'], ['5', '6', '7', '8']]
    print(lista)
    print("Vamos substituir esse itens !!!")

    lista[0].remove('4')
    lista[1].remove('8')
    lista[0].insert(3, input("Digite o valor para substituir: "))
    lista[1].insert(3, input("Digite o valor para substituir: "))
    print(lista)


main()
