
def numVelasAniversario ():
    alturaVelas = []
    n = int(input("Digite a sua idade: "))
    if n <= 1 and n >= 10 ** 5:
        print("Entrada invalida, por favor digite um numero valido")
        n = int(input("Digite a sua idade: "))

    altura = input("digite o tamanho das velas: ").split()
    for i in range(n):
        alturaInt = int(altura[i])
        if alturaInt >= 1 and alturaInt <= 10 ** 7:
            alturaVelas.append(alturaInt)

    maiorValor = max(alturaVelas)
    quantMaior = alturaVelas.count(maiorValor)

    print(f"A maior vela e {maiorValor} com a quantidade de {quantMaior} velas")

numVelasAniversario()
