def main():
    listaAlumnos=[]
    print("programa que solicita calificaciones de alumnos")
    num_alumnos_str = input("cantidad de alumnos:")
    while not num_alumnos_str.isdigit():
        print("numero no valido, Intenta de nuevo")
        num_alumnos_str = input("cantidad de alumnos")
    num_alumnos = int(num_alumnos_str)
    for i in range(1, num_alumnos+1):
        print("calificaciones del alumno"+str(i)+":")
        lista_calif = solicitaCalificaciones(5)
        listaAlumnos.append(lista_calif)
        print()
    promedios =[]
    cont=1
    for elem in listaAlumnos:
        prom= promedio(elem)
        promedios.append(prom)
        print("promedio de calificaciones del alumno" +str(cont)+":"+str(round(prom)))
        cont+=1
    maximo = max(promedios)
    cont=1
    for prom in promedios:
        if prom== maximo:
            alumno=cont
        cont+=1
    print("el alumno"+str(alumno)+"tiene el promedio mayor")

    print(listaAlumnos)
    
