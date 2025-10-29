file = open("odbiorcy.txt", "r").read().split()
naj = 0
for x in range(0,len(file)):
    if file.count(file[x]) > int(file[naj]):
        naj = x
print(file[naj])

