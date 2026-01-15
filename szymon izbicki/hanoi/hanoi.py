def hanoi(n, start, dest):
    if n == 0:
        return
    middle = 6 - (start + dest)
    hanoi(n - 1, start, middle)
    draw(start, dest)
    hanoi(n - 1, middle, dest)


def draw(start, dest):
    #mapowanie numerow kijkow do literek
    kijki = {1: a, 2: b, 3: c}

    #przenoszenie krazka na kijek na zasadzie stacków
    krazek = kijki[start].pop()
    kijki[dest].append(krazek)

    print(start, "->", dest, "\n")

    #rysuj plansze
    A, B, C = a[:], b[:], c[:]
    h = max(len(A), len(B), len(C))
    A += [" "] * (h - len(A))
    B += [" "] * (h - len(B))
    C += [" "] * (h - len(C))

    for i in range(h - 1, -1, -1):
        print(f"{A[i]} \t {B[i]} \t {C[i]}")
    print("-"*10)

#input + init
n = int(input("Hanoi dla liczby krazkow n = "))
a, b, c = [x for x in range(n, 0, -1)], [], []

#plansza poczatek
for elem in a[::-1]:
    print(elem)
print("-"*10)

#game
hanoi(n, 1, 3)
print("solved!")