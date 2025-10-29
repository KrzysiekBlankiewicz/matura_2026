def znajdzlidera(arr):
    lider = None
    ile = 0
    for i in arr:
        if ile == 0:
            lider = i
            ile = 1
        elif i == lider:
            ile += 1
        else:
            ile -= 1

    ile = sum(1 for x in arr if x == lider)
    if ile > len(arr) // 2:
        return lider

print(znajdzlidera([1,2,2,2,2,2,2,3,1,1])) 
   
