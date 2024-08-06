#ivan araluce nava A00949193
# calcular las raices con condicionales y valors de x1 y x2
#29/01/2016

print("ingrese los valores que se le piden")
a=input("ingrese el valor de a:")
b=input("ingrese el valor de b:")
c=input("ingrese el valor de c:")
a_str=int(a)
b_str=int(b)
c_str=int(c)

import math
x1= (-b_str+(b_str**2-4*a_str*c_str)**.5/(2*a_str))
x2= (-b_str-(b_str**2-4*a_str*c_str)**.5/(2*a_str))
if(a_str==0 and b_str==0):
    print("la ecuacion no tiene solucion")
if (a==0):
    raiz= (a_str-c_str)/b_str
    print("raiz individual:", raiz)
else:
    if (a_str>0 and b_str>0 and c_str>0):
        print("valor de x1:", x1)
        print("valor de x2:", x2)
    if (a_str<0 and b_str<0 and c_str<0):
        print("no hay raices reales")
    else:
        raiz_repetida= (a_str-b_str)/(2*a_str)
    
