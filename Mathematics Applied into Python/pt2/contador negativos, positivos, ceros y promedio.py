#ivan araluce nava A00949193
#Ciclos While
#ejercicio 6, numeros positivos, negativos, ceros y promedio.
contpos=0
contneg=0
contcero=0
contnumeros=1
sumapos=0
sumaneg=0

numeros=int(input("ingresa la cantidad de numeros que va a usar:"))
while(contnumeros<=numeros):
    numero=int(input("numeros:"))
    contnumeros=contnumeros+1
    if(numero>0):
        contpos=contpos+1
        sumapos=sumapos+numero
    else:
        if(numero<0):
            contneg=contneg+1
            sumaneg=sumaneg+numero
        else:
            
            contcero=contcero+1
promediopos=sumapos/contpos
promedioneg=sumaneg/contneg
print("numeros positivos:", contpos, "Promedio:", promediopos)
print("numeros negativos:", contneg, "Promedio:", promedioneg)
print("ceros:", contcero)

        

