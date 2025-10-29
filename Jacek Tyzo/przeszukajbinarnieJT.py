def bubblesort(lista):
    k = 0
    n = len(lista) - 1
    for j in range(n): 
        i = 0  
        while i < n - k:
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp 
            i += 1
        k += 1
    return lista


def przeszukajbinarnie(lista, x):
    lista = bubblesort(lista)
    l = 0
    p = len(lista) - 1
    while l <= p:
        center = (l + p) // 2
        if lista[center] == x:
            return center
        elif lista[center] < x:
            l = center + 1
        else:
            p = center - 1


lista = [9, 2, 3, 4, 5, 6, 7, 8, 9]
print(przeszukajbinarnie(lista, 7))
