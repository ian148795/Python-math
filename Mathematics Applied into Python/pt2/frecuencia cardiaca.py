#ivan araluce nava
#frecuencia cardiaca
#ciclos for

def frecuenciaCardiaca(y):
    fc=208-0.7*y
    return fc
#programa principal
for x in range(20,41,2):
    frecuencia=frecuenciaCardiaca(x)
    print(x,frecuencia)
    
