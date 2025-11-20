def szereg_silni(n):
    suma = 0
    silnia = 1
    for i in range(1, n + 1):
        silnia = silnia * i
        suma += silnia
    return suma