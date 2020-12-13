num = int(input("Digite um numero para ver sua Tabuada: "))

def tabuada ():

    for i in range (0, 11):
        resultado = i * num
        print(" {} X {} = {}".format(num, i, resultado))



tabuada()

