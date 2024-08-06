cont_num=0
suma_num=0

numero=1
while numero!=0:
    numero = int(input("introduce el numero:"))
    suma_num= suma_num+numero 
    if numero !=0:
        cont_num= cont_num+1

print(cont_num)
print(suma_num)
print("el promedio:", suma_num/cont_num)
