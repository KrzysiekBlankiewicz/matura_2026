def wartoscwielomianu(wsp, x):
    wynik = 0
    potega = 1
    for w in wsp:
        wynik += w * potega
        potega *= x
    return wynik
print(wartoscwielomianu([2, 3, 5], 2))
