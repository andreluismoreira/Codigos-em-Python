def main():
    listaDeClientes = []
    while True:
        clientesFiado = {"nome": None, "divida": None, "endereço": None}

        opcao = input("*=*=* Escolha uma opção desejada *=*=* \n"
                      "1- Cadastro de clientes\n"
                      "2- Atualização de divida\n"
                      "3- Remoção de cliente\n"
                      "4- Busca por nome\n"
                      "5- Sair\n")

        if opcao == "1":
            nome = input("Digite o nome do liso: ")
            clientesFiado['nome'] = nome
            divida = input(f"Digite o prego do {clientesFiado['nome']}: ")
            clientesFiado['divida'] = divida
            endereco = input("Digite o endereço do liso: ")
            clientesFiado['endereço'] = endereco
            listaDeClientes.append(clientesFiado)
            print(listaDeClientes)

        elif opcao == "2":
            nome = input("Digite o nome do liso: ")
            divida1 = input(f"Digite o novo prego: ")
            for i in listaDeClientes:
                if nome in i.values():
                    i['divida'] = divida1

            print(listaDeClientes)

        elif opcao == "3":
            nome = input("Digite o nome do liso: ")
            for i in listaDeClientes:
                if nome in i.values():
                    listaDeClientes.remove(i)
                    print("liso removido da lista de prego")
                    print(listaDeClientes)

        elif opcao == "4":
            nome = input("Digite o nome do liso: ")
            for i in listaDeClientes:
                if nome in i.values():
                    print(i)
                else:
                    print("esse liso nao deve aqui")

        elif opcao == "5":
            break

        else:
            print("entrada invalida tente novamente")


main()
