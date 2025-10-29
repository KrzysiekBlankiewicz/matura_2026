def addbin(a, b):
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    s = ''
    c = '0'  
    for i in range(len(a) - 1, -1, -1):
        ile = [a[i], b[i], c]
        jedynki = ile.count('1')  

        if jedynki == 0:
            s = '0' + s
            c = '0'
        elif jedynki == 1:
            s = '1' + s
            c = '0'
        elif jedynki == 2:
            s = '0' + s
            c = '1'
        else: 
            s = '1' + s
            c = '1'

    if c == '1':
        s = '1' + s

    return s
print(addbin('101010' , '1111'))
