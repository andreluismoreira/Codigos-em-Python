
def main():
    sair = False
    registro = [ ]
    while sair != True:
        entrada = input("digite uma entrada para registro: ")
        registro.append(entrada)
        controle = input("deseja continuas (N/S): ").upper()

        if controle == "N":
            sair = True
            print(registro)

main()
