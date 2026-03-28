def a():
    with open("galerie.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].split()[0]

    miasta = dict.fromkeys(file, 0)
    for elem in file:
        miasta[elem] += 1

    print(miasta)

def b():
    klucze = []

    with open("galerie.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].split()
        klucze.append(file[i][1])


    pow = dict.fromkeys(klucze, 0)
    lok = dict.fromkeys(klucze, 0)
    for elem in file:
        for i in range(2, len(elem)- 1,  2):
            pow[elem[1]] += int(elem[i])*int(elem[i+1])
        lok[elem[1]] += 70 - elem[2:].count("0")//2

    print("BA")
    print(pow)
    print(lok)

    print("BB")
    for elem in pow:
        if pow[elem] == max(pow.values()):
            print(elem, max(pow.values()))
        if pow[elem] == min(pow.values()):
            print(elem, min(pow.values()))

def c():
    klucze = []

    with open("galerie.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].split()
        klucze.append(file[i][1])

    lok = {}
    for elem in klucze:
        lok[elem] = set()

    for elem in file:
        for i in range(2, len(elem)- 1,  2):
            lok[elem[1]].add(int(elem[i])*int(elem[i+1]))

    max_len, max_key, min_len, min_key = 0, None, 1000000000000, None
    for elem in lok:
        if len(lok[elem]) > max_len:
            max_len = len(lok[elem])
            max_key = elem
        if len(lok[elem]) < min_len:
            min_len = len(lok[elem])
            min_key = elem

    print(max_key, max_len)
    print(min_key, min_len)


a()
b()
c()
