import random
x = random.randint(1,100)
print("Adivina el numero que estoy pensando, del 1 al 100")
numero =int(input("introduce el numero:"))

while numero!=x:
    if (numero<x):
        print("estas abajo")
    elif(numero>x):
        print("estas arriba")
    numero=int(input("introduce el numero:"))
print("es correcto")
