funcionarios = []
salarios = []
salarioBruto = 0


def menuInicar():
    global salarioBruto
    entrada = 0

    while entrada != "3":
        print("1- Cadastrar funcionario")
        print("2- Imprimir Contra-cheque")
        print("3- Sair")
        entrada = input()

        if entrada == "1":
            funcionario = input("Digite o seu nome para cadastro: ")
            funcionarios.append(funcionario)
            salarioBruto = float(input("Digite seu salario Bruto: "))
            salarios.append(salarioBruto)
        elif entrada == "2":
            Inss(salarioBruto)
            Irf(salarioBruto)
            print(funcionarios)
            indice = int(input("Digite o indice do funcionario que voce deseja imprimir o contra cheque: "))
            print("nome: " + funcionarios[indice])
            print("salario Bruto: {}".format(salarios[indice]))
            print("O desconto do inss e: {}".format(inss))
            print("O desconto do irf e: {}".format(irf))
            salarioLiquido = salarioBruto - inss - irf
            print("O salario liquido e de: {}".format(salarioLiquido))
        elif entrada == "3":
            break
        else:
            print("Valor nao encontrado tente novamente ")
            print("1- Cadastrar funcionario")
            print("2- Imprimir Contra-cheque")
            print("3- Sair")
            entrada = input()


def Inss(salarioBruto):
    global inss

    if salarioBruto <= 1045:
        inss = 78.38
    elif 1045 < salarioBruto <= 2089.60:
        inss = 172.39
    elif 2089.60 < salarioBruto <= 3134.40:
        inss = 297.77
    elif 3134.40 < salarioBruto <= 6101.60:
        inss = 558.95
    else:
        inss = 713.10


def Irf(salarioBruto):
    global irf

    if salarioBruto <= 1903.98:
        irf = 0
    elif 1903.98 < salarioBruto <= 2826.65:
        irf = 142.80
    elif 2826.65 < salarioBruto <= 3751.05:
        irf = 354.80
    elif 3751.05 < salarioBruto <= 4664.68:
        irf = 636.13
    else:
        irf = 896.36


menuInicar()
