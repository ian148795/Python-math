#ivan araluce nava A00949193
#guess number 1-100
#11/03/2016

import random
x=random.randint(1,100)
print("adivina el numero que estoy pensando del 1 al 100")
numero=int(input("introduce el numero:"))
cont=0
while numero!=x:
    cont=cont+1
    if(numero<x):
        print("estas abajo")
    elif(numero>x):
        print("estas arriba")
    numero=int(input("introduce el numero:"))
print("CORRECTO!","\t", "solo te tomo:",cont,"veces!")
