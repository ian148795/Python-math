def series(n):
    suma=o
    for i in range(1,n+1):
        cubo=(i+1)*3-i**3
        suma=suma+cubo
    return suma
#programa principal
resultado=series(1)
print(1,resultado)
for x in range(3,13,3):
    resultado=series(x)
    print(x,resultado)
    
