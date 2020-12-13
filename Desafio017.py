import math
oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = (math.hypot(oposto, adjacente))
print('Para o cateto oposto dado {} e o adjacente {} a hipotenusa e {:.2f}'.format(oposto, adjacente, hipotenusa))
