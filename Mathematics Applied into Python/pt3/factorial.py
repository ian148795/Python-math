def factorial(n):
    multiplicacion = 1
    for i in range(2,n+1):
        nultiplicacion = multiplicacion*i
    return multiplicacion

#programa principal
num = int(input("numero del factorial:"))
for i in range(1,8):
    factorial(i)
    print(i)
    
