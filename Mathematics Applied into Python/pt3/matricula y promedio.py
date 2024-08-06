#programa para obtener el promedio
#paso 1 pedir las calificaciones del alumno
#paso 2 imprimir la matricula del alumno
#mostra el promedio

matric_str = input ("matric:")

calif1_str = input ("calif1:")
calif2_str = input ("calif2:")
calif3_str = input ("calif3:")
calif1_int = int (calif1_str)
calif2_int = int (calif2_str)
calif3_int = int (calif3_str)

resultante = (calif1_int+calif2_int+calif3_int)/3

print ("promedio de calificaciones de ",matric_str, "es", resultante)
