def lider(wyrazy):
    #slownik
    unique = {}
    for elem in wyrazy:
        if elem not in unique:
            unique[elem] = {"liczba": elem, "ilosc": 0}
        unique[elem]["ilosc"] += 1

    #max(unique["ilosc"]))
    max_elem = {"liczba": 0, "ilosc": 0}
    for elem in unique.values():
        if elem["ilosc"] > max_elem["ilosc"]:
            max_elem["liczba"] = elem["liczba"]
            max_elem["ilosc"] = elem["ilosc"]

    #czy idol?
    if max_elem["ilosc"] > len(wyrazy) // 2:
        return max_elem["liczba"]
    else:
        return False