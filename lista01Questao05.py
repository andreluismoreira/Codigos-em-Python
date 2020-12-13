print('---Lados do retangulo---')
Lado=int(input('Digite o comprimento do lateral do retangulo: '))
Base=int(input('Digite o comprimento da base do retangulo: '))
perimetro=((2*Lado)+(2*Base))
area=Lado*Base
print('O valor escolhido para o lado escolhido foi {}, para a base foi {}, tendo como perimetro {} e {} como area'.format(Lado,Base,perimetro,area))