#ivan araluce nava A00949193
#basel
#ejercicios for
#11/03/2016

def basel(n):
    suma=0
    for i in range(1, n+1):
        suma=suma+1/i**2
    return suma

#programa principal
for i  in range(1,5):
    num=10**i
    resultado=basel(num)
    print(num,resultado)
