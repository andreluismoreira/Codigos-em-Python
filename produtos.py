
item1 = input("digite o valor so produto 1: ")
item2 = input("digite o valor so produto 2: ")
item3 = input("digite o valor so produto 3: ")

if item1 < item2 and item3:
    print("O item 1 e o mais indicado seu valor e {}".format(item1))
elif item2 < item1 and item3:
    print("O item 2 e o mais indicado seu valor e {}".format(item2))
else:
    print("O item 3 e o mais indicado seu valor e {}".format(item3))
