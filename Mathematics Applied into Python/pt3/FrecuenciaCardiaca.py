def frecuenciaCardiaca(edad):
    frecuencia = 208-0.7*edad
    return frecuencia
#programa principal
for i in range(20,61,2):
    print((i , frecuencia))
