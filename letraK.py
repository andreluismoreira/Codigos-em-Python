def main ():

    nome = input("digite seu nome: ")
    n1 = float(input("digite sua 1º nota: "))
    n2 = float(input("digite sua 2º nota: "))

    media = (n1 + n2) / 2

    if media < 7:
         print(f"Ola {nome}, sua media foi {media} e voce esta Reprovado")
    elif media == 10:
         print(f"Ola {nome}, sua media foi 10 e voce foi Aprovado com Honras")
    else:
         print(f"Ola {nome}, sua media foi {media} e voce esta Aprovado")


main()