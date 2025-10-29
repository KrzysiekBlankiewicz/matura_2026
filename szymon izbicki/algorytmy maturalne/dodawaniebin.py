def dodawaniebin(a, b):
    a, b = str(a), str(b)

    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b = "0" + b
    elif len(b) > len(a):
        for i in range(len(b) - len(a)):
            a = "0" + a

    wynik = ""
    carry = 0

    for i in range(len(a) - 1, -1, -1):
        suma = int(a[i]) + int(b[i]) + carry

        if suma == 0:
            wynik = "0" + wynik
            carry = 0
        elif suma == 1:
            wynik = "1" + wynik
            carry = 0
        elif suma == 2:
            wynik = "0" + wynik
            carry = 1
        elif suma == 3:
            wynik = "1" + wynik
            carry = 1

    if carry == 1:
        wynik = "1" + wynik

    return wynik
