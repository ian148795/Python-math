def numero(a):
    suma=0
    for i in range(1,a+1):
        suma+=i
    return suma
#programa principal
for i in range(1,5):
    print(i, numero(i))
    
