with open("odbiorcy.txt") as f:
    file = f.readlines()
for i in range(len(file)):
    file[i] = int(file[i].strip())

lista = []
for i in range(len(file)):
    lista.append(i+1)

ile = 0
for i in lista:
    if i not in file:
        ile += 1
print(ile)
        
