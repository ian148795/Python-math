#ejercicio 1
num = int(input("escriba el numero de la tabla 2:"))
cont = 1
while(num<=10):
    print(num, "x", cont, "=", num*cont)
    cont+=1

    




#ejercicio 2
num = int(input("seleccione la tabla que quiere:"))

while(num<1 or num>10):
    print("Su numero no es valido, intente de nuevo")
    num=int(input("dame el numero de la tabla que deseas 1-10"))

cont = 1
while (cont<=10):
    print(num, "x", cont, "=", num*cont)
    cont+=1
                     
