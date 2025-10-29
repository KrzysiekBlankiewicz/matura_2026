with open("odbiorcy.txt") as f:
    file = f.readlines()
for i in range(len(file)):
    file[i] = int(file[i].strip())

lista = []
for i in range(len(file)):
    lista.append(i+1)

runda = 1
stop = 0
przekierowania = file[:]
while stop == 0:
    for i in range(len(file)):
        if file[i] == lista[i]:
            stop = 1
            print (runda , file[i])
            break
    runda += 1
    new_file = []
    for i in file:
        new_file.append(przekierowania[i-1])
    file = new_file
        
