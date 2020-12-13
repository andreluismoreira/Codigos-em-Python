
def manipulacaodelista():
    lista = []
    for i in range(0, 5):
        data = int((input("Digite o ano de nascimento do seu amigo: ")))
        lista.append(data)

    lista.sort(reverse=True)
    print(lista)

    lista.sort()
    print(lista)


manipulacaodelista()
