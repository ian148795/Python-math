nombre = input("cual es tu nombre:")

cali1=int(input("ingresa tu calificacion del primer parcial:"))
cali2=int(input("ingresa tu calificacion del segundo parcial:"))
cali_proyecto=int(input("ingresa tu calificacion del proyecto final:"))
prom1=(cali1 + cali2)/2
cali2_proyecto= cali_proyecto*.20
final= prom1*.80 + cali2_proyecto
print("la calificacion de", nombre, "es de:", final)

