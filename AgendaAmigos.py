def adicionaramigos(agenda):
    print("Deseja adicionar um amigo a sua agenda ?")
    print(agenda)
    nome = input("Digite o nome do seu amigo: ")
    niver = input("Digite a data de aniversario do seu amigo: ")
    lista = [nome, "data: {}".format(niver)]
    agenda.append(lista)
    print(agenda)


def removeramigos(agenda):
    print("Deseja remover um amigo da sua agenda ?")
    print(agenda)
    i = int(input("digite o indice da pessoa que deseja remover: "))
    agenda.pop(i)
    print(agenda)


def main():
    agenda = list()
    opcao = ""
    while opcao != 0:

        print("#*#*#*#*#* Agenda de Amigos *#*#*#*#*#")
        print("Menu de Opções: \n"
              "1- Adicionar Amigo \n"
              "2- Remover Amigo \n"
              "0- Sair \n")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionaramigos(agenda)
        elif opcao == 2:
            removeramigos(agenda)
        else:
            print("Opção invalida, tente novamente !!!")

main()