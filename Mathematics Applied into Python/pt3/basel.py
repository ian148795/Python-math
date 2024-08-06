def basel(n):
    suma=0
    for i in range(1,n):
        residuo=1%n**2
        if residuo==0:
            suma=suma+1%n**2
    if suma==o:
            return True
    else:
            return False

#programa principal
for i in range(1,10000):
    if basel(i):
        print(i)
        
