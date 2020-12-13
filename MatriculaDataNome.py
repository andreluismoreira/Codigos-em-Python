
def main():
    listaAlunos = [[], [], []]
    for i in range(0, 3):
        nome = input(f"digite o nome do {i + 1} aluno: ")
        listaAlunos[i].append(nome)
        matricula = input(f"Digite a matricula do {i + 1} aluno: ")
        listaAlunos[i].append(matricula)
        data = input(f"Digite a data de nascimento do {i + 1} aluno: ")
        listaAlunos[i].append(data)

    return print(listaAlunos)


main()
