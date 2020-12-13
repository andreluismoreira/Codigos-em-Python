dado = input('Digite algo:')
print('O tipo primitivo do dado digitado e:', type(dado))
print('So tem espaços', dado.isspace())
print('E um numero ?', dado.isnumeric())
print('E alfabetico ?', dado.isalpha())
print('E alfanumerico ?', dado.isalnum())
print(' Esta em maiusculas ?', dado.isupper())
print('Esta em minusculas ?', dado.islower())
print('Esta capitalizada ?', dado.istitle())


