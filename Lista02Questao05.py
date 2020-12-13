age = int(input('Digite a sua idade: '))
if age < 5:
    print('Nao possui idade suficiente')
elif age >= 5 and age <= 7:
    print('INFANTIL A')
elif age > 7 and age <= 10:
    print('INFANTIL B')
elif age > 10 and age <=13:
    print("JUVENIL A")
elif age > 13 and age <= 17:
    print('juvenil B')
else:
    print('SENIOR')

