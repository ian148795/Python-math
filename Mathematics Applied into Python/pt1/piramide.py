#ivan araluce nava A00949193
#ciclos for
#piramid

def piramide(n):
    suma=0
    for i in range(1, n+1):
        cuad=i**2
        suma=suma+cuad
    return suma
#programa principal
for x in range(1,16):
    print(x, piramide(x))
    
