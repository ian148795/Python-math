#Ivan Araluce Nava A00949193

def menor (a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        num = b

    else:
        num = c
    return num

def  menu():
    print(",)Numero Mayor\n z) Numero Menor ")
    opcion = int(input("opcion:"))
    return opcion

#programa principal

f = menu
a = int(input("inserte el primer numero"))
b = int(input("inserte el segundo numero"))
c = int(input("inserte el tercer numero"))

if f ==1:
    print("el mayor es" , Mayor(a,b,c))

else:
    print("El menor es" , menor(a,b,c))


    
    
