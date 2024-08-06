#22/01/2016
#ivan araluce nava A00949193
#nomina
#calcular el pago de un empleado

pago_hora=int(input("Pago por hora:"))
horas = int(input("horas trabajadas:"))
horas_extras=int(input("horas extras:"))
pagoN= pago_hora*horas
pagoextra= horas_extras*(pago_hora*1.5)
pago_total=pagoN+pagoextra
print("pago total: $", pago_total)
