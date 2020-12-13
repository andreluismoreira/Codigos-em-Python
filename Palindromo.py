def main():
    entrada = str(input("digite aqui para descobrir se e palindromo: ")).strip().upper()
    listaInvertida = ""
    for c in range(len(entrada) - 1, 0 - 1, -1):
        listaInvertida += entrada[c]

    if entrada == listaInvertida:
        print(f'O numero digitado {entrada} e um palindormo !')
    else:
        print(f'O numero digitado {entrada} NÃO e um palindormo !')


main()
