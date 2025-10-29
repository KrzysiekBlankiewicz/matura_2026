def wartoscwielomianu(wsp, x):
    w = 0
    n = len(wsp)
    for i in range(n):
        w += wsp[i] * (x ** (n - i - 1))
    return w


def miejscezerowe(wsp, a, b, d):
    while abs(b - a) > d:
        srodek = (a + b) / 2
        fs = wartoscwielomianu(wsp, srodek)
        if fs > 0:
            b = srodek
        elif fs < 0:
            a = srodek
        else:
            return srodek

    return (a + b) / 2



    
print(miejscezerowe([1, -3, 2], 1.5, 3, 0.0001))   
