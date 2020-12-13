#função retorna 0 em caso de erro
def calc_media(primNota, segNota, terNota, mediaNota):
    if mediaNota == 'a':
        return (primNota + segNota + terNota)/3
    elif mediaNota == 'p':
        return (primNota * 5 + segNota * 3 + terNota * 2)/10
    elif mediaNota == 'h':
        return 3/(1/primNota + 1/segNota + 1/terNota)
    else:
        return 0


print(f"O valor da media escolhida e: {calc_media(10, 7, 9, 'a'):.2f}")
print(f"O valor da media escolhida e: {calc_media(10, 7, 9, 'p'):.2f}")
print(f"O valor da media escolhida e: {calc_media(10, 7, 9, 'h'):.2f}")
