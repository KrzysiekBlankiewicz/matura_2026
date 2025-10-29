file = open("odbiorcy.txt", "r").read().split()
licznik = len(file)
print(licznik)
suma = 0
for x in range(1,licznik+1):
    print(x)
    if str(x) not in file:
        suma+=1
print(suma)