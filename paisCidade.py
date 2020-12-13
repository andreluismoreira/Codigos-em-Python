def cidade():
    cidades = []
    ind = int(input("Digite quantas cidades vc vai inserir: "))
    for i in range(0, ind):
        city = input("Digite o nome da Cidade: ")
        cidades.append(city)
    print(cidades)


def pais():
    paises = list()
    indc = int(input("Digite quantos Países vc vai inserir: "))
    for i in range(0, indc):
        contry = input("Digite o nome do Pais: ")
        paises.insert(indc, contry)
    print(paises)


cidade()
pais()
