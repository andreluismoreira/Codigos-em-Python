def diaDoProgramador():
    ano = int(input("digite um ano entre 1700 e 2700: "))

    if ano >= 1700 and ano <= 1917:
        print("Esse ano utiliza o calendario Juliano")
        if ano % 4 == 0:
            print(f"O dia do programador foi na data: 12/09/{ano}")
        else:
            print(f"O dia do programador foi na data: 13/09/{ano}")
    elif ano == 1918:
        print(f"O dia do programador foi na data: 26/09/{ano}")
    elif ano >= 1919 and ano <= 2700:
        print("Esse ano utiliza o calendario Gregoriano")
        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            print(f"O dia do programador foi na data: 12/09/{ano}")
        else:
            print(f"O dia do programador foi na data: 13/09/{ano}")
    else:
        print("entrada invalida !!! ")


diaDoProgramador()