def czyanagram(a, b):
    if len(a) != len(b):
        return False
    a, b = list(a), list(b)
    for l in a:
        if l in b:
            b.remove(l)
        else:
            return False
    if b == []:
        return True

print(czyanagram('qwerty' , 'ytrewq'))
