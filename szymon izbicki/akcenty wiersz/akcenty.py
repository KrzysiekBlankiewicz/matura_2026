def samogloski(tekst):
    samogloski = ["a", "e", "o", "i", "y", "u", " "]
    wiersz = []
    for i in range(len(tekst)):
        if tekst[i] in samogloski:
            wiersz.append(tekst[i])
            if tekst[i+1] in samogloski: i += 1

    return wiersz

def akcenty(file):
    #find accents
    for i in range(len(file), 0, -1):
        if file[i] == " ":
            if file[i] == file[i-1]:
                file[i-1] = "*"
            else:
                file[i-2] = "*"

    #fill out the rest with "-" and remove spaces
    for i in range(len(file)):
        if file[i] == " ":
            del file[i]
        elif file[i] != "*":
            file[i] = "-"

    return file

with open("lokomotywa.txt") as f:
    file = f.read()
    file = list(file)
    for i in range(len(file)):
        if file[i] == "\n":
            file[i] = " "

file = samogloski(file)
file = akcenty(file)
print(file)