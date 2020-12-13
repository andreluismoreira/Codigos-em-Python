def produto(int1, int2):
  return (int1 * 2) + (int2 / 2)


def soma(int1, real):
  return (int1 * 3) + real


def potencia(real):
  return real ** 3


def main():
  int1 = int(input("digite um numero inteiro: "))
  int2 = int(input("digite um numero inteiro: "))
  real = float(input("digite um numero inteiro: "))

  print("O produto do dobro do 1° mais a metade do 2° e: {}".format(produto(int1, int2)))
  print("A soma do triplo do 1° com o terceiro e: {}".format(soma(int1, real)))
  print("A potncia do 3° ao cubo e: {}".format(potencia(real)))


main()