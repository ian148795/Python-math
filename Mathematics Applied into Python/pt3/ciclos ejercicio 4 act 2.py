#promedio de las calificaciones

numero_total = int(input("promedio total de las materias:"))

#inicializar variables
suma_calificaciones = 0
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
