def czy_anagram(a, b):
    if len(a) != len(b):
        return False

    a, b = list(map(str.strip, a)), list(map(str.strip, b))

    for elem in a:
        if elem not in b:
            return False
        for desired in b:
            if elem == desired:
                b.remove(desired)
    return True