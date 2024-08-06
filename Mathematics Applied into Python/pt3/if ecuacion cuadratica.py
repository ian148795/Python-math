# Ivan Araluce Nava A00949193
#Ecuacion Cuadratica
#26/08/2015

import math

a_str = input("valor de a:")
b_str = input("valor de b:")
c_str = input("valor de c:")
a = int(a_str)
b = int(b_str)
c = int(c_str)

if a==0 and b==0:
    print("no tiene solucion")

else:
    if a==0:
        print("la raiz individual es:" , -c/b)
    else:
        discriminante = b**2-4*a*c
        if discriminante>0:
            raiz1 = -b+math.sqrt(b**2-4*a*c)/(2*a)
            raiz2 = -b-math.sqrt(b**2-4*a*c)/(2*a)
            print("desplegar las dos raices" , raiz1 , raiz2)
        else:
            if discriminante<0:
                print("no hay raices reales")
            else:
                raizrepetida = -b/(2*a)
                print("desplegar la raiz repetida" , raizrepetida)
                
            
