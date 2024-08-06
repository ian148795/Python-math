#Ivan Araluce Nava A00949193
#ejercicio 4
#30/08/2015

edad_str = input("edad:")
categoria_str = input("tipo de enfermedad:")
tiempo_str = input("cuantos dias:")
edad = int(edad_str)
categoria = int(categoria_str)
tiempo = int(tiempo_str)

if categoria == 1:
    categoria= 250
    formula = categoria*tiempo
if categoria == 2:
    categoria= 160
    formula = categoria*tiempo
if categoria == 3:
    categoria= 200
    formula = categoria*tiempo
if categoria == 4:
    categoria= 320
    formula = categoria*tiempo
if edad>=30 and edad<=40:
    imp = formula*0.10

print("El costo diario por enfermedad es:",categoria)
print("El costo por",tiempo,"dias es:",formula)
print("El costo adicional por edad es:",imp)
print("El costo total es:",formula+imp)
