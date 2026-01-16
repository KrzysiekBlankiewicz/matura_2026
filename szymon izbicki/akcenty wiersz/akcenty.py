def samogloski(tekst):
    samogloski = ["a", "e", "o", "i", "y", "u"]
    wiersz = []

    i = 0
    while i < len(tekst):
        if tekst[i] == "\n":
            wiersz.append("\n")
            i += 1
        elif tekst[i] == " ":
            wiersz.append(" ")
            i += 1
        elif tekst[i] in samogloski:
            wiersz.append(tekst[i])
            if i + 1 < len(tekst) and tekst[i + 1] in samogloski:
                i += 2
            else:
                i += 1
        else:
            i += 1
    return wiersz


def akcenty(file):
    for i in range(len(file)-1, -1, -1):
        if file[i] == "\n":
            continue

        if file[i] == " ":
            if i - 1 >= 0 and file[i - 1] == " ":
                file[i - 1] = "*"
            else:
                if i - 2 >= 0 and file[i - 2] != "\n":
                    file[i - 2] = "*"

    for i in range(len(file)-1,-1,-1):
        if file[i] == " ":
            del file[i]
        elif file[i] != "*" and file[i] != "\n":
            file[i] = "-"

    return file


with open("lokomotywa.txt") as f:
    file = f.read()
    file = file.replace("\n", " \n")
    file = list(file)

file = samogloski(file)
file = akcenty(file)

print("".join(file))
