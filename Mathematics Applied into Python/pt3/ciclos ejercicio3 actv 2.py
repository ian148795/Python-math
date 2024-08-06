#solicitar al usuario el numero total
numero_total = int(input("numero que se quiere sacar el promedio"))

#inicializar variable
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0

contador = 1
while(contador<=numero_total):
    numero = int(input("numero:"))
    if(numero<0):
        suma_negativos=suma_negativos+numero
        contador_negativos=contador_negativos+1
    elif(numero>0):
        suma_positivos=suma_positivos+numero
        contador_positivos=contador_positivos+1
    contador+=1
print("suma negativos:", suma_negativos)
print("suma positivos:", suma_positivos)

#promedio de las calificaciones

numero_total_materias = int(input("promedio total de las materias:"))

#inicializar variables
suma_calificacions = 0
materias_aprobadas = 0
materias_reprobadas = 0
calificaciones_reprobadas = 0

cont = 0
while (cont<numero_total):
    calificacion = int(input("escriba la calificacion:"))

    if (calificacion<0 or calificacion>100):
        print("error de calificacion, favor de volver a introducir")

    elif(calificacion>=70 and calificacion <=100):
        suma_calificaciones = suma_calificaciones+calificacion
        materias_aprobadas = materias_aprobadas+1
        cont= cont+1

    elif(calificacion>0 and calificacion<70):
        calificaciones_reprobadas = calificaciones_reprobadas+calificacion
        materias_reprobadas = materias_reprobadas+1
        cont = cont+1

promedio_total = (suma_calificaciones+calificaciones_reprobadas)/numero_total
print("promedio general:", promedio_total)
print("materias aprobadas:", materias_aprobadas)
print("materias reprobadas:", materias_reprobadas)
