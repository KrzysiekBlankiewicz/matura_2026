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

a()