def perfect(n):
    suma=0
    for i in range(1,n):
        residuo=n%i
        if residuo==0:
            suma=suma+i
    if suma==n:
        return True
    else:
        return False
    
#programa principal
for i in range(1,10000):
    if perfect(i):
        print(i)
