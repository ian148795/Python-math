# Ivan Araluce Nava A00949193
#raiz y reciproco
# 24/08/2015

import math

number = int(input("valor del numero:"))

if number<0:
    print("los numeros negativos no tienen raiz")

else:
    print("la raiz es", math.sqrt(number))

if number==0:
    print ("no es valido el numero 0")

else:
    print("el reciproco es", 1/number)
    
          
