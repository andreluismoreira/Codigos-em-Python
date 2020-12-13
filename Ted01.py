def potencia (base, exponencial):
    pot = 1
    if base == 0:
        return 0
    elif exponencial == 0:
        return 1
    elif exponencial <= -1:
        return (1/base) ** (exponencial * -1)
    else:
        for count in range(exponencial):
            pot *= base
        return pot


print(f'2 elevado a 3 e: {potencia(2, 3)}')
print(f'3 elevado a 2 e: {potencia(3, 2)}')
print(f'3 elevado a -2 e: {potencia(3, -2):.2}')
print(f'3 elevado a 0 e : {potencia(3, 0)}')
print(f'0 elevado a 2 e : {potencia(0, 2)}')
print(f'10 elevado a 2 e : {potencia(-10, 4)}')
print(f'0 elevado a 2 e : {potencia(-10, 5)}')