def cores():
    cor = []
    cont = int(input("digite quantas cores voce quer adicionar: "))
    for i in range(0, cont):
        cores = input("digite uma cor: ")
        cor.append(cores)
        if cores == "vermelho":
            cor.remove(cores)
        else:
            print("A cor digitada nao foi vermelha !!!")
    print(cor)


cores()
