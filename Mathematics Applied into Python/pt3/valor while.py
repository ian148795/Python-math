suma=0
continuar='s'
print("\nSuma de numeros/n")
while(continuar=='s'):
    num=int(input("dame un numero:"))
    suma = suma + num
    continuar= input("¿desea continuar(s/n)?")
    continuar=continuar.lower()

print("\nEl valor de la suma es", suma)

    
    
