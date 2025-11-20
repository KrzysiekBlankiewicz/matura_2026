def a():
    with open("dane.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].rstrip()

    slowa = {}
    for i in range(len(file)):
        if file[i] not in slowa:
            slowa[file[i]] = 1
        else:
            slowa[file[i]] += 1

    wiecej_niz_raz = 0
    najwiecej_wystapien = 0
    slowo_najczestsze = None
    for slowo, counter in slowa.items():
        if counter > 1:
            wiecej_niz_raz += 1
        if counter > najwiecej_wystapien:
            najwiecej_wystapien = counter
            slowo_najczestsze = slowo


    print(f"wiecej niz dwa razy: {wiecej_niz_raz}")
    print(f"najwiecej westapien: {slowo_najczestsze}, wystapil {najwiecej_wystapien} razy")

def b():
    with open("dane.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].rstrip()

    counter = 0
    for elem in file:
        if int(elem, 16)%2 == 0:
            counter += 1
    print(counter)

def c():
    with open("dane.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].rstrip()

    counter = 0
    for elem in file:
        if elem == elem[::-1]: counter += 1

    print(counter)

print("a:")
a()
print("b:")
b()
print("c:")
c()