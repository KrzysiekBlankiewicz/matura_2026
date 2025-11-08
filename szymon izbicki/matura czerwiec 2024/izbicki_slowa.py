def a():
    with open("slowa.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()

    counter = 0
    for elem in file:
        for i in range(len(elem)-2):
            if elem[i] == "k" and elem[i+2] == "t":
                counter += 1

    print(counter)

def encrypt(a):
    result = ""
    for letter in a:
        result += chr((ord(letter)-ord('a')+13)%26+ord('a'))
    return result

def palindrom(a, b):
    return a == b[::-1]

def b():
    with open("slowa.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()

    counter = 0
    najdluzsze = ""

    for w in file:
        if encrypt(w) == w[::-1]:
            counter += 1
            if len(w) > len(najdluzsze):
                najdluzsze = w

    print(counter)
    print(najdluzsze)

def idol(a):
    for i in range(len(a)):
        if a.count(a[i]) >= len(a) / 2:
            return True
    return False


def c():
    with open("slowa.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()

    for elem in file:
        if idol(elem):
            print(elem)

print("a:")
a()
print("b:")
b()
print("c:")
c()