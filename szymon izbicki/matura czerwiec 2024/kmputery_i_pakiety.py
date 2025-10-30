def a():
    with open("odbiorcy.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = int(file[i].strip())

    counter = 0
    for i in range(len(file)+1):
        if i+1 not in file:
            counter += 1

    print(counter)

def b():
    with open("odbiorcy.txt") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = int(file[i].strip())

    start = []
    for i in range(len(file)):
        start.append(i+1)

    for i in range(1, len(file)+1):
        dest = [0] * len(file)
        for j in range(1, len(file)+1):
            sender = start[j-1]
            recipient = file[sender-1]
            dest[j-1] = recipient
        start = dest

        for k in range(1, len(file) + 1):
            if start[k - 1] == k:
                print("runda", i, "numer", k, sep=" ")
                return

    print("brak")

print("a:")
a()
print("b:")
b()