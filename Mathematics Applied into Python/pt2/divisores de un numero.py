#ivan araluce nava A00949193
#15/03/2016
#divisores de un numero
import math
def division(n):
    resi=n/1
    return resi
def raiz(n):
    resii=math.sqrt(n)
    return resii

#programa principal
numero=int(input("numero:"))
while(numero!=0):
    div=division(numero)
    for i in range(1,numero+1):
        resiii=numero/i
        resiii=numero%i
        if(resiii==0):
            print("divisores:",div,i)
    numero=int(input("numero:"))
print("gracias por usar nuestros servicios")
