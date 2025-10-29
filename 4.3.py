file = open("odbiorcy.txt", "r").read().split()
print(len(file))
lista = []
pakiet = 0
for x in file:
    pakiet+=1
    where = x
    for y in range(2,100):
        #print(file[int(where)-1],x)
        if file[int(where)-1] == str(x):
            lista.append([y-1, pakiet])
        where = int(file[int(where)-1])
naj = 0
for x in range(len(lista)):
    if lista[x][0] < lista[naj][0]:
        naj = x
print(lista[naj][0],lista[naj][1])
