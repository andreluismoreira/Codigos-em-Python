def cadastrodenovoslivros():
    novoLivro = []
    titulo = input("Digite o titulo do livro: ")
    novoLivro.append(titulo)
    ano = input("Digite o ano do livro: ")
    novoLivro.append(ano)
    quantidade = input("Digite a quantidade de exemplares")
    novoLivro.append(quantidade)
    categoria = input("O livro e fisico ou digital ?: ")
    novoLivro.append(categoria)
    tematica = input("Qual o tema do livro: ")
    novoLivro.append(tematica)


def titulosreservaveis():
    reservaveis = list()
    titulo = input("Digite o titulo do livro: ")
    reservaveis.append(titulo)
    ano = input("Digite o ano do livro: ")
    reservaveis.append(ano)
    categoria = input("O livro e fisico ou digital ?: ")
    reservaveis.append(categoria)
    tematica = input("Qual o tema do livro: ")
    reservaveis.append(tematica)





print(" ### MENU DE OPÇÕES ###")
print("Digite a numeração do serviço que voce deseja:"
      " 1- Cadastro de funcionario"
      " 2- Login no Sistema"
      " 3- Cadastro de novos livros"
      " 4- Titulos Reservados"
      " 5- Atualizar quantidade de titulo"
      " 6- Remover titulos desatualizados"
      " 7- Buscar exemplares"
      " 8- Importar dados"
      " 9- Obter status do titulo"
      "10- Gerar relatorio do acervo"
      "11- Gerar relatorio por categoria de livro"
      "12- Gerar relatorio por tematica do livro"
      "13- Sair do sistema")
resposta = input("Digite a opção desejada: ")

"""
while resposta != 13:

    if resposta == 1:

    elif resposta == 2:

    elif resposta == 3:
        cadastrodenovoslivros()
    elif resposta == 4:
        titulosreservaveis()
    elif resposta == 5:

    elif resposta == 6:

    elif resposta == 7:

    elif resposta == 8:

    elif resposta == 9:

    elif resposta == 10:

    elif resposta == 11:

    elif resposta == 12:

    elif resposta == 13:
        break
    else:
        print("Entrada invalida tente novamente !!!")
        resposta = input("Digite a opção desejada: ") """



