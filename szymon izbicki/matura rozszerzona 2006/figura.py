def f(x): return -(x**2)/50

def g(x): return 1+(x**2)/100-x/200

def a():
    suma = 0
    x = 10
    h = 0.01
    while x > 0:
        #przyblizanie 10 * 100 = 10000 trapezami
        suma += ((-f(x)+g(x))+(-f(x+h)+g(x+h)))*h*0.5
        x -= h
    print(round(suma * 100)/100)

def b():
    szukamy = True
    c = 100
    while szukamy:
        #szukamy punktu oddalenogo o 100 od prawej krawedzi figury ktorego "wysokosc" bedzie miescila 26 i miala zabas zeby wierzochlki wyladowly na punktach o x calkowitych
        if g(c-100)-f(c-100)>26+1:
            szukamy = False
        c+=1
    print(c)

print("a")
a()
print("b")
b()