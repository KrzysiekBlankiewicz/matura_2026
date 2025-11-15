def wyszukiwanie_bin(lista, cel, start, end):
    middle = (start+end)//2
    if start > end: return "not found"
    if lista[middle] == cel:
        return middle
    elif lista[middle] < cel:
        return wyszukiwanie_bin(lista, cel, middle+1, end)
    else:
        return wyszukiwanie_bin(lista, cel, start, middle-1)

lista = [1, 3, 5, 7, 9, 11, 13]
print(wyszukiwanie_bin(lista, 7, 0, len(lista)-1))