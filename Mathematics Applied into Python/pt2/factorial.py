#ivan araluce nava A00949193
#factorial
#ciclos for

def factorial(n):
    if(n==0):
        return 1
    else:
        multiplicacion=1
        for i in range(1, n+1):
            multiplicacion=multiplicacion*i
        return multiplicacion
#programa principal
for x in range(0,11):
    print(x,"\t", factorial(x))
    
